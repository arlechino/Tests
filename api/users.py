import requests
from utilities.config_parser import ReadConfig


class User:

    def __init__(self):
        self.__base_url = ReadConfig.get_base_api_url()

    def create(self, data:dict) -> requests.Response:
        return requests.post(f'{self.__base_url}/api/users', data=data)

    def getById(self, user_id:int = 12) -> requests.Response:
        return requests.get(f'{self.__base_url}/api/users/{user_id}')

    def putchUpdate(self, user_id:int, data:dict) -> requests.Response:
        return requests.patch(f'{self.__base_url}/api/users/{user_id}', data=data)

    def putUpdate(self, user_id:int, data:dict) -> requests.Response:
        return requests.put(f'{self.__base_url}/api/users/{user_id}', data=data)

    def delete(self, user_id:int) -> requests.Response:
        return requests.delete(f'{self.__base_url}/api/users/{user_id}')