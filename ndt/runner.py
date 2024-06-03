""" NDT Runner
"""
from dotenv import load_dotenv
from mods import config

if __name__ == '__main__':
    load_dotenv()
    args = config.get_parser()
    print(args)
    cfg = config.get_config()
    print(cfg)

    print("hello")
