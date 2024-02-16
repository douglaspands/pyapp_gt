ARG USER=app


# Node Builder
FROM node:iron-bookworm as node_builder

COPY ./www /var/build/www

RUN cd /var/build/www && npm install
RUN cd /var/build/www && npm run build


# Python Base
FROM python:3.12.2-bookworm as python_base
ARG USER

ENV TZ=America/Sao_Paulo \
    LC_ALL=pt_BR.UTF-8 \
    LC_CTYPE=pt_BR.UTF-8 \
    LANG=pt_BR.UTF-8 \
    LANGUAGE=pt_BR.UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PYTHONWARNINGS="ignore:Unverified HTTPS request" \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt update -qq && \
    apt install -y --no-install-recommends locales tzdata && \
    ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    dpkg-reconfigure --frontend noninteractive tzdata && \
    sed -i -e 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen pt_BR.UTF-8 && update-locale LANG=pt_BR.UTF-8 LC_ALL=pt_BR.UTF-8 && \
	apt autoremove -y && apt clean -y && rm -rf /var/lib/apt/lists/* && \
    useradd --home /home/${USER} ${USER}


# App Release
FROM python_base as app_release
ARG USER
ARG GIT_COMMIT

LABEL GIT_COMMIT=${GIT_COMMIT}

USER ${USER}
WORKDIR /home/${USER}

ENV DJANGO_SETTINGS_MODULE="django_core.settings.production"

COPY --chown=${USER}:${USER} ./requirements.txt ./requirements.txt
RUN pip install --user -r ./requirements.txt && \
    pip cache purge && rm -Rf ./.cache && rm -f ./requirements.txt

COPY --chown=${USER}:${USER} ./manage.py ./manage.py
COPY --chown=${USER}:${USER} ./django_core ./django_core

COPY --chown=${USER}:${USER} ./www/views ./www/views
COPY --chown=${USER}:${USER} ./www/templates ./www/templates
COPY --chown=${USER}:${USER} ./www/forms ./www/forms
COPY --chown=${USER}:${USER} ./www/urls ./www/urls
COPY --chown=${USER}:${USER} ./www/__init__.py ./www/apps.py ./www/
COPY --from=node_builder --chown=${USER}:${USER} /var/build/www/static ./www/static
RUN ln -sf ./www/static ./static
