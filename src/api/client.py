import dlt
from dlt.sources.rest_api import RESTAPIConfig, ClientConfig, rest_api_source
from loguru import logger
from pathlib import Path
from src.utils.yaml import ConfigParser


class Client:
    def __init__(self):
        self.config: RESTAPIConfig = dict(
            client=ClientConfig, resources=[], resource_defaults={}
        )
        logger.debug(f"Client created: {self.config}")

    def set_resource_defaults(self, resource_defaults: dict):
        self.config["resource_defaults"] = resource_defaults

    def register_resource(self, resource: dict):
        self.config["resources"].append(resource)

    def unregister_resource(self, resource: dict):
        self.config["resources"].remove(resource)

    def set_client_config(self, base_url, auth, paginator):
        logger.debug(f"Client configuration set: {base_url}, {auth}, {paginator}")
        self.config["client"] = dict(base_url=base_url, auth=auth, paginator=paginator)


class UpbankClient(Client):
    def get_source(self, path: Path):
        config_parser = ConfigParser(path)
        config = config_parser.get_config()
        config["client"]["auth"].update(
            {"token": dlt.secrets[config["client"]["auth"]["token"]]}
        )
        self.set_client_config(**config["client"])

        for resource in config["resources"]:
            self.register_resource(resource)

        return rest_api_source(self.config, name="upbank")
