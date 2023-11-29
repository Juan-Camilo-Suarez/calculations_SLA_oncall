import logging
import sys

import requests

from configs import Config


class PrometheusRequest:

    def __init__(self, config: Config) -> None:
        self.prometheus_api_url = config.prometheus_api_url

    def lastValue(self, query: str, time: str, default: str = "") -> str:
        try:
            response = requests.get(
                self.prometheus_api_url + "/api/v1/query", params={"query": query, "time": time}
            )
            content = response.json()
            if not content:
                return default
            if len(content["data"]["result"]) == 0:
                return default
            return content["data"]["result"][0]["value"][1]
        except Exception as error:
            return default
            logging.error(error)


def setup_logging(config: Config) -> None:
    logging.basicConfig(
        stream=sys.stdout,
        level=config.log_level,
        format="%(asctime)s %(levelname)s %(message)s",
    )
