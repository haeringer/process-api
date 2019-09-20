import pytest
import os
import main


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
    assert b'processes_url' in response.data


def test_processes(client):
    response = client.get('/processes')
    assert b'pid' in response.data


def test_own_process_not_in_results(client):
    pid_current = os.getpid()
    response = client.get('/processes')
    response_str = response.data.decode("utf-8")
    assert '"pid": {},'.format(str(pid_current)) not in response_str
