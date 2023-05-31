store = {}
Assignment = open('assignment.txt', 'w')
user = input('Write your full name here:')
if(Assignment.write('Username: '+ user +'\n')):
    store['Name'] = user
    password = input('Type in your pin:')
    Assignment.write('Password: '+ password + '\n')
    store['Pin'] = password
    print('Successful')
else:
    print('Error-Unavailable')
