import logging

import mysql

from configs import Config


class Mysql:
    def __init__(self, config: Config) -> None:
        logging.info("connecting to Mysql")
        self.connection = mysql.connector.connect(
            host=config.mysql_host,
            user=config.mysql_user,
            passwd=config.mysql_password,
            auth_plugin='mysql_native_password'
        )
        self.table_name = 'indicators'
