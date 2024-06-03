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

def get_loggers():
    """ get_loggers
    """

    return {
        "runner": {"level": "DEBUG", "handlers": ["stderr", "stdout", "file"]},
        "sql_io": {"level": "DEBUG", "handlers": ["stderr", "stdout", "file"]},
        "models": {"level": "DEBUG", "handlers": ["stderr", "stdout", "file"]},
        "logging_config": {"level": "DEBUG", "handlers": ["stderr", "stdout", "file"]},
        "config": {"level": "DEBUG", "handlers": ["stderr", "stdout", "file"]},
        "file_io": {"level": "DEBUG", "handlers": ["stderr", "stdout", "file"]},
        "sqlalchemy.engine.Engine": {
            "level": "WARNING",
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
        "loggers": get_loggers(),
    }
    logging.config.dictConfig(logging_config)

def initialize_logging(ndtargs, cfg):
    """
    Initialize logging for the application.
    """
    configure_logging(cfg)
    #logger.debug("NR Host Schema: %s", Host.schema())
    logger.critical("Passed Arguments: %s", ndtargs)
    logger.error("Passed Arguments: %s", ndtargs)
    #logger.debug("SqlAlchemy Version: %s", sqlalchemy.__version__)
