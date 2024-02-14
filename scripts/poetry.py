import os
import sys


def run_shell(cmd: str) -> int:
    print(f"$ {cmd}")
    return os.system(cmd)


def run_makerequirements():
    cmd = "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    sys.exit(run_shell(cmd))
