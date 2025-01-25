from pathlib import Path
import yaml


class ConfigParser:
    def __init__(self, path: Path):
        self.path = path

    def get_config(self):
        with open(self.path) as f:
            config = yaml.safe_load(f)
        return config
