or_password = '12345'
password = input('Input password:')

if password == or_password:
    print('Pass OK')
    name = input('Input name:')
    if name == 'Admin':
        print('Grant access')
    elif name == 'Operator':
        print('Only view')
    elif name == 'User':
        print('No Control')
    else:
        print('No access')
else:
    print('Pass Error')
