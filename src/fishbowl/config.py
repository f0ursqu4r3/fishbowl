from typing import Any
import tomli


class Config:
    def __init__(self):
        with open("config.toml", "rb") as f:
            self.config = tomli.load(f)

    def get(self, key: str, default: Any = None) -> Any:
        # key is a dot-separated string
        keys = key.split(".")
        value = self.config
        for k in keys:
            value = value.get(k, default)
        return value


config = Config()
