import logging

import mysql.connector

from configs import Config


class Mysql:
    def __init__(self, config: Config) -> None:
        logging.info("connecting to Mysql")

        self.connection = mysql.connector.connect(
            host=config.mysql_host,
            port=config.mysql_port,
            user=config.mysql_user,
            passwd=config.mysql_password,
            auth_plugin='mysql_native_password'
        )
        self.table_name = 'indicators'

        cursor = self.connection.cursor()

        logging.info("creating db")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config.mysql_db_name}")
        cursor.execute('USE sla')