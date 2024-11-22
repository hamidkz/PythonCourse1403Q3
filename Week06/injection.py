users = [
    {
        "username": 'hamid',
        "password": '123'
    },
    {
        "username": 'zahra',
        "password": '111'
    },
]

def authenticate(username: str, password: str):
    for user in users:
        if user.get('username') == username and user.get('password') == password:
                return True
    return False        

username = input('Username: ')
password = input('Password: ')
print(authenticate(username=username, password=password))

