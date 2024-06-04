""" NDT Runner
"""
import argparse
import logging
import configparser
from pathlib import Path

logger = logging.getLogger("config")

def get_parser():
    """
    Get the parser for the application.
    """
    myparser = argparse.ArgumentParser()
    myparser.add_argument("-v", "--verbosity", action="count", default=0,
                        help="increase output verbosity")
    myparser.add_argument("-s", "--sqllog", action="store_true", default=False,
                        help="sqllog")
    myparser.add_argument("-p", "--purge", action="store_true", default=False,
                        help="purge")
    myparser.add_argument("-l", "--loglevel", action="store", default="DEBUG",
                        help="log level")
    return myparser.parse_args()

def construct_path(*makepath):
    """ construct_path
    """
    return str(Path(__file__).parent.parent.joinpath(*makepath))

def get_config(args_passed):
    """
    Load the application configuration from the config.ini file.

    Returns:
        A dictionary containing the configuration values.
    """
    #TODO: add the parsed in args to the config

    cfg = configparser.ConfigParser()
    config_file = construct_path('data\\config', 'config.ini')
    #print(config_file)
    cfg.read(config_file)
    if args_passed.loglevel != cfg.get('logging', 'app_level'):
        logging_level =  args_passed.loglevel
    else:
        logging_level = cfg.get('logging', 'app_level')

    config_dict = {
        'db_uri': f"{cfg.get('db','uri')}/{cfg.get('db','path')}/{cfg.get('db','name')}",
        'net_user': cfg.get('network', 'user'),
        'net_pass': cfg.get('network', 'password'),
        'logging_file': construct_path(cfg.get('logging', 'path'), cfg.get('logging', 'name')),
        'logging_level': logging_level,
        "runner_level": cfg.get("logging", "runner_level"),
        "ndt_crawler_level": cfg.get("logging", "ndt_crawler_level"),
        "sql_io_level": cfg.get("logging", "sql_io_level"),
        "models_level": cfg.get("logging", "models_level"),
        "logging_config": cfg.get("logging", "logging_config"),
        "config_level": cfg.get("logging", "config_level"),
        "file_io_level": cfg.get("logging", "file_io_level"),
        "sqlalchemy_engine_level": cfg.get("logging", "sqlalchemy_engine_level"),
        'error_file': construct_path(cfg.get('logging', 'path'), cfg.get('logging', 'error')),
        'input_csv':construct_path(cfg.get('input_data','path'),cfg.get('input_data','devices')),
        'nornir_config': construct_path('data', 'nornir.yaml'),

    }

    return config_dict

if __name__ == '__main__':
    args = get_parser()
    config = get_config(args_passed=None)
