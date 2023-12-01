import logging
import time
from datetime import datetime

from configs import Config
from db import Mysql
from prometheus_connection import setup_logging, PrometheusRequest


def main():
    config = Config()
    setup_logging(config)
    db = Mysql(config)
    prom = PrometheusRequest(config)

    logging.info("Starting sla cheker")

    while True:
        logging.debug("Run Prober")

        unixtimestamp = int(time.time())
        date_format = datetime.utcfromtimestamp(unixtimestamp).strftime('%Y-%m-%d %H:%M:%S')

        # prober to create user
        value = prom.lastValue('increase(prober_create_user_scenario_success_total[1m])', unixtimestamp, 0)
        value = int(float(value))
        db.save_indicator(name='prober_create_user_scenario_success_total',
                          slo=1,
                          value=value,
                          is_bad=value < 1,
                          time=date_format)

        value = prom.lastValue('increase (prober_create_user_scenario_success_fail_total[1m])', unixtimestamp, 100)
        value = int(float(value))
        db.save_indicator(name='prober_create_user_scenario_success_fail_total',
                          slo=0,
                          value=value,
                          is_bad=value > 0,
                          time=date_format)

        value = prom.lastValue('prober_create_user_scenario_duration_seconds', unixtimestamp, 2)
        value = float(value)
        db.save_indicator(name='prober_create_user_scenario_duration_seconds',
                          slo=0.1,
                          value=value,
                          is_bad=value > 0.1,
                          time=date_format)

        # prober to create team
        value = prom.lastValue('increase(prober_create_team_scenario_success_total[1m])', unixtimestamp, 0)
        value = int(float(value))
        db.save_indicator(name='prober_create_team_scenario_success_total',
                          slo=1,
                          value=value,
                          is_bad=value < 1,
                          time=date_format)

        value = prom.lastValue('increase (prober_create_team_scenario_fail_total[1m])', unixtimestamp, 100)
        value = int(float(value))
        db.save_indicator(name='prober_create_team_scenario_success_fail_total',
                          slo=0,
                          value=value,
                          is_bad=value > 0,
                          time=date_format)

        value = prom.lastValue('prober_create_team_scenario_duration_seconds', unixtimestamp, 2)
        value = float(value)
        db.save_indicator(name='prober_create_team_scenario_duration_seconds',
                          slo=0.1,
                          value=value,
                          is_bad=value > 0.1,
                          time=date_format)

        # prober add user to user
        value = prom.lastValue('increase(prober_add_user_to_team_scenario_success_total[1m])', unixtimestamp, 0)
        value = int(float(value))
        db.save_indicator(name='prober_add_user_to_team_scenario_success_total',
                          slo=1,
                          value=value,
                          is_bad=value < 1,
                          time=date_format)

        value = prom.lastValue('increase (prober_add_user_to_team_scenario_fail_total[1m])', unixtimestamp, 100)
        value = int(float(value))
        db.save_indicator(name='prober_add_user_to_team_scenario_success_fail_total',
                          slo=0,
                          value=value,
                          is_bad=value > 0,
                          time=date_format)

        value = prom.lastValue('prober_add_user_to_team_scenario_duration_seconds', unixtimestamp, 2)
        value = float(value)
        db.save_indicator(name='prober_add_user_to_team_scenario_duration_seconds',
                          slo=0.1,
                          value=value,
                          is_bad=value > 0.1,
                          time=date_format)
        logging.warning(f"Waiting for Prober{config.scrape_interval} seconds for next loop")
        time.sleep(config.scrape_interval)


if __name__ == "__main__":
    main()
