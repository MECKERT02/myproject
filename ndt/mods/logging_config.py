""" NDT Logging Config
"""
import logging
import logging.config
from colorlog import ColoredFormatter

logger = logging.getLogger("logging_config")

def get_formatters():
    """ get_formatters 
    """

    return {
        "simple": {"format": "%(levelname)-8s - %(message)s"},
        "verbose": {
            "format": "%(asctime)s - %(name)-5s - %(levelname)-8s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "colored": {
            "()": ColoredFormatter,
            "format": 
                "%(log_color)s%(asctime)s %(name)s:"+
                "%(levelname)-8s%(reset)s %(blue)s%(message)s _.(%(lineno)d)",
            "datefmt": "%m-%d %H:%M:%S",
            "reset": True,
            "log_colors": {
                "DEBUG": "purple",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white"
            },
        },
    }

def get_handlers(cfg):
    """ get_handlers
    """

    return {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": cfg["logging_level"],
            "formatter": "colored",
            "stream": "ext://sys.stdout"
        },
        "stderr": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "verbose",
            "filename": cfg["error_file"],
            "mode": "w"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "verbose",
            "filename": cfg["logging_file"],
            "mode": "w"
        },
        "console2": {
            "class": "logging.StreamHandler",
            "formatter": "colored",
        },
        "file2": {
            "class": "logging.FileHandler",
            "filename": cfg["logging_file"],
            "formatter": "verbose",
            "level": "DEBUG",
            "mode": "w"
        },
    }

def get_loggers(cfg):
    """ get_loggers
    """

    return {
        "runner": {"level": cfg["runner_level"], "handlers": ["stderr", "stdout", "file"]},
        "ndt_crawler":{"level": cfg["ndt_crawler_level"], "handlers": ["stderr", "stdout", "file"]},
        "sql_io": {"level": cfg["sql_io_level"], "handlers": ["stderr", "stdout", "file"]},
        "models": {"level": cfg["models_level"], "handlers": ["stderr", "stdout", "file"]},
        "logging_config":{"level": cfg["logging_config"], "handlers": ["stderr", "stdout", "file"]},
        "config": {"level": cfg["config_level"], "handlers": ["stderr", "stdout", "file"]},
        "file_io": {"level": cfg["file_io_level"], "handlers": ["stderr", "stdout", "file"]},
        "sqlalchemy.engine.Engine": {
            "level": cfg["sqlalchemy_engine_level"],
            "formatter": "colored",
            "handlers": ["stderr", "stdout", "file"],
        },
    }

def configure_logging(cfg):
    """
    Configure the logging settings for the application.
    """
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": get_formatters(),
        "handlers": get_handlers(cfg),
        "loggers": get_loggers(cfg),
    }
    logging.config.dictConfig(logging_config)
    #logger.debug(logging_config)
    return logging_config

def initialize_logging(cfg):
    """
    Initialize logging for the application.
    """
    logcfg=configure_logging(cfg)
    return logcfg
    #logger.debug("NR Host Schema: %s", Host.schema())
    #logger.critical("Passed Arguments: %s", ndtargs)
    #logger.error("Passed Arguments: %s", ndtargs)
    #logger.debug("SqlAlchemy Version: %s", sqlalchemy.__version__)
