from http import HTTPStatus


def test_read_root_return_ok_and_message(client):
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'olá mundo'}


def test_create_user(client):
    response = client.post(  # userSchema
        '/users/',
        json={
            'username': 'joao1',
            'password': 'joao2',
            'email': 'joao@joao.com',
        },
    )
    # check return correct status code
    assert response.status_code == HTTPStatus.CREATED

    # check UserPublic
    assert response.json() == {
        'username': 'joao1',
        'email': 'joao@joao.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'joao1',
                'email': 'joao@joao.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '1221',
            'username': 'testename',
            'email': 'teste@teste.com',
        },
    )
    assert response.json() == {
        'username': 'testename',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted.'}
