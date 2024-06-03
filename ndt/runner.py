""" NDT Runner
"""
import logging
from dotenv import load_dotenv
from mods import config
from mods import logging_config
from ndt_crawler import ndt_crawler

logger = logging.getLogger("runner")

if __name__ == '__main__':
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

    print("hello")
