import logging

from environs import Env

env = Env()
env.read_env()


class Config(object):
    prometheus_api_url = env("PROMETHEUS_API_URL", 'http://158.160.122.18:9090')
    scrape_interval = env.int("SCRAPE_INTERVAL", 60)
    log_level = env.log_level("LOG_LEVEL", logging.INFO)

    mysql_host = env("MYSQL_HOST", 'localhost')
    mysql_port = env.int("MYSQL_PORT", '3306')

    mysql_user = env("MYSQL_USER", 'root')
    mysql_password = env("MYSQL_PASS", '1234')

    mysql_db_name = env("MYSQL_DB_NAME", 'sla')
