import configparser

from CONST_PATH import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configuration.ini')

class ReadConfig:
    @staticmethod
    def get_base_ui_url() -> str:
        return config.get('app_info', 'base_ui_url')

    @staticmethod
    def get_base_api_url() -> str:
        return config.get('app_info', 'base_api_url')

    @staticmethod
    def get_driver_id():
        return int(config.get('browser', 'browser_id'))
