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

        cursor = self.connection.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS %s (
                    datetime datetime not null default NOW(),
                    name varchar(255) not null,
                    slo float(4) not null,
                    value float (4) not null,
                    is_bad bool not null default false
                )
            """ % (self.table_name))

        cursor.execute("""
                ALTER TABLE %s ADD INDEX (datetime)
            """ % (self.table_name))

        cursor.execute("""
                ALTER TABLE %s ADD INDEX (name)
            """ % (self.table_name))

    def save_indicator(self, name, slo, value, is_bad=False, time=None):
        cursor = self.connection.cursor()
        sql = f"INSERT INTO {self.table_name} (name, slo, value, is_bad, datetime) VALUES (%s, %s, %s, %s, %s)"
        val = (name, slo, value, int(is_bad), time)
        cursor.execute(sql, val)
        self.connection.commit()
