""" NDT Runner
"""
import logging
from dotenv import load_dotenv
from mods import config
from mods import logging_config
from ndt_crawler import ndt_crawler

logger = logging.getLogger("runner")

if __name__ == '__main__':
    try:
        load_dotenv()
        ndtargs = config.get_parser()
        #print(args)
        cfg = config.get_config()
        #print(cfg)
        logcfg=logging_config.initialize_logging(ndtargs, cfg)
        #logging_config.initialize_logging(cfg)
        logger.debug("Command line args: %s", ndtargs)
        logger.debug("Logger Configuration: %s", logcfg)
        logger.debug("App Configuration: %s", cfg)

        ndt_crawler(ndtargs, cfg, logcfg)
    except FileNotFoundError as e:
        logger.critical("File not found: %s", e)
        raise
    except ValueError as e:
        logger.critical("Value error: %s", e)
        raise
    except Exception as e:
        logger.critical("Unhandled exception: %s", e)
        raise

