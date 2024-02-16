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
