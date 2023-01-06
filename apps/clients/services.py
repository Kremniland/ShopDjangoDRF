import requests


def get_token(name: str, password: str) -> str:
    '''Получаем токен'''
    r = requests.post('http://127.0.0.1:8000/auth/token/login/', {
        'username': name,
        'password': password
        })
    token = r.json()['auth_token']
    return token

def get_data(url: str, token: str) -> list:
    '''Получаем данные из url по token'''
    r = requests.get(url, headers={
        'Authorization': 'Token ' + token
        })
    return r.json()


if  __name__ == '__main__':
    token = get_token('admin', '1234')
    print(token)

    data = get_data('http://127.0.0.1:8000/api/clients/', token)

    for i in data:
        print(type(i))
        print(i)