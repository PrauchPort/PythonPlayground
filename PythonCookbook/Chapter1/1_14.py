from operator import attrgetter


class User():
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"User('{self.user_id}')"


users = [User(24), User(12), User(35), User(9)]

print(users)

print(sorted(users, key=attrgetter('user_id')))

print(sorted(users, key=lambda x: x.user_id))
