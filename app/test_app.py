import pytest

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
    assert b'PID' in response.data
