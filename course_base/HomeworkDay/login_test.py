def login_v1():
    flag = False
    for i in range(3):
        if flag:
            continue

        username = input('Enter your username: ')
        if username != 'admin':
            print('Invalid username')
            continue
        else:
            for i in range(3):
                password = input('Enter your password: ')
                if password != 'admin':
                    print('Invalid password')
                    continue
                else:
                    flag = True
                    break
            else:
                break
    else:
        if flag:
            print('Success login,Hello admin')
        else:
            print('Fail login, username or password failed')


def login_v2():
    for i in range(3):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        if password == 'admin' and username == 'admin':
            print('Success login,Hello admin')
            break
        else:
            print('Fail login, username or password failed')
            print(f'你还有{2 - i}次机会')

login_v2()