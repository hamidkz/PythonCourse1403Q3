emails = ['hamid.kz@gmail.com', 'hamidkz@systemgroup.net', 'hamid.kazemzadeh@afraway.org']
# output: ['hamid.kz', 'hamidkz', 'hamid.kazemzadeh']

def get_username(email):
    email_lst = email.split('@')
    username = email_lst[0]
    return username

result = map(get_username, emails)
print(list(result))


