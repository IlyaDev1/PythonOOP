from lib import User


users = [User()]
for i in range(10):
    users.append(User(users[i]))

for i in range(len(users)):
    print(users[i].__dict__)

users[5].Name = 'Noname'
print(users[5].Name)
