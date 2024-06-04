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
        #TODO: add code to create dir structure if it doesnt exist
        #TODO: Create default config files
        
        ndtargs = config.get_parser()
        cfg = config.get_config(ndtargs)
        logcfg=logging_config.initialize_logging(cfg)
        logger.debug("Command line args: %s", ndtargs)
        logger.debug("Logger Configuration: %s", logcfg)
        logger.debug("App Configuration: %s", cfg)
        logger.info("check fo updates in %s", cfg["input_csv"])

        ndt_crawler(ndtargs, cfg)
    except FileNotFoundError as e:
        logger.critical("File not found: %s", e)
        raise
    except ValueError as e:
        logger.critical("Value error: %s", e)
        raise
    except Exception as e:
        logger.critical("Unhandled exception: %s", e)
        raise
