import pytest

from CONST_PATH import JSON_WITH_UTF_8
from api.users import User
from utilities.random_data import RandomData
from http import HTTPStatus

@pytest.mark.API
class TestsUsers:

    __user: User = User()
    __test_data: RandomData = RandomData()
    __user_id: list = [0]

    def tests_create_user(self):
        name = self.__test_data.first_name()
        job = self.__test_data.job()
        response = self.__user.create(data = {'name': name, 'job': job})
        assert response.status_code == HTTPStatus.CREATED
        assert response.headers.get('Content-Type') == JSON_WITH_UTF_8
        # TODO pydantic or json schema for validations response
        assert response.json().get('name') == name
        assert response.json().get('job') == job
        assert int(response.json().get('id')) > 1
        self.__user_id[0] = int(response.json().get('id')) > 1

    def test_get_user_by_id(self):
        response = self.__user.getById()
        assert response.status_code == HTTPStatus.OK
        assert response.headers.get('Content-Type') == JSON_WITH_UTF_8
        assert type(response.json().get('data')) == dict
        assert type(response.json().get('support')) == dict

    def test_update_user_patch(self):
        name = self.__test_data.first_name()
        job = self.__test_data.job()

        uid = self.__user_id[0] if self.__user_id[0] != 0 else 12
        response = self.__user.putchUpdate(user_id=uid, data = {'name': name, 'job': job})
        assert response.status_code == HTTPStatus.OK
        assert response.headers.get('Content-Type') == JSON_WITH_UTF_8
        # TODO pydantic or json schema for validations response
        assert response.json().get('name') == name
        assert response.json().get('job') == job

    def test_update_user_put(self):
        name = self.__test_data.first_name()
        job = self.__test_data.job()

        uid = self.__user_id[0] if self.__user_id[0] != 0 else 12
        response = self.__user.putUpdate(user_id=uid, data={'name': name, 'job': job})
        assert response.status_code == HTTPStatus.OK
        assert response.headers.get('Content-Type') == JSON_WITH_UTF_8
        # TODO pydantic or json schema for validations response
        assert response.json().get('name') == name
        assert response.json().get('job') == job

    def test_delete_user(self):
        uid = self.__user_id[0] if self.__user_id[0] != 0 else 12
        response = self.__user.delete(user_id=uid)
        assert response.status_code == HTTPStatus.NO_CONTENT
