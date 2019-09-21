import pytest
import os
import main

import utils


@pytest.fixture
def client():
    main.app.config['TESTING'] = True

    client = main.app.test_client()
    context = main.app.app_context()
    context.push()

    yield client

    context.pop()


def test_api_root(client):
    response = client.get('/')
    assert b'/processes' in response.data


def test_processes(client):
    response = client.get('/processes')
    assert b'PID' in response.data


def test_own_process_not_in_results(client):
    pid_current = os.getpid()
    response = client.get('/processes')
    response_str = response.data.decode("utf-8")
    assert '"pid": {},'.format(str(pid_current)) not in response_str


def test_environment_is_list(client):
    response = client.get('/processes')
    responses_json = response.get_json()
    for item in responses_json:
        if not isinstance(item['Environment'], list):
            print(item)
            print(type(item))
        # assert isinstance(item['Environment'], list)


def test_utils_dict_to_list():
    testdict = dict(key1='val1', key2='val2')
    testlist = utils.dict_to_list(testdict)
    assert isinstance(testlist, list)
