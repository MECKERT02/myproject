""" NDT Runner
"""
import logging
from dotenv import load_dotenv
from mods import config
from mods import logging_config

logger = logging.getLogger("runner")

if __name__ == '__main__':
    load_dotenv()
    ndtargs = config.get_parser()
    #print(args)
    cfg = config.get_config()
    #print(cfg)
    logging_config.initialize_logging(ndtargs, cfg)
    #logging_config.initialize_logging(cfg)
    logger.info("Command line args: %s", ndtargs)
    logger.info("Configuration: %s", cfg)
    print("hello")
