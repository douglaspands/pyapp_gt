import os


def run_shell(cmd: str) -> int:
    print(f"$ {cmd}")
    return os.system(cmd)


def make_requirements():
    cmd = "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    run_shell(cmd)


def make_secretkey():
    import secrets

    print(secrets.token_hex())


def run_www_watch():
    cmd = "cd www && npm run watch"
    run_shell(cmd)


def rum_emailserver_start():
    cmd = "cd .docker && docker compose -f emailserver.docker-compose.yml up -d && docker compose -f emailserver.docker-compose.yml logs -f"
    run_shell(cmd)


def rum_emailserver_stop():
    cmd = "cd .docker && docker compose -f emailserver.docker-compose.yml down -v"
    run_shell(cmd)
