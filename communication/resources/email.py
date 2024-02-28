from dataclasses import dataclass


@dataclass
class Email:
    sender: str
    to: list[str]
    subject: str
    message: str


__all__ = ("Email",)
