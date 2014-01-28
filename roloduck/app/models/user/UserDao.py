from app.models.user import User
class UserDao(object):

    def __init__(self, database):
        self.db = database
        self.user = database.user

    def find_users(self):
        list = []
        for each_user in self.user.find():
            list.append({'name': each_user['name'],
                         'email': each_user['email']})
        return list

    def find_user_by_id(self, id):
        user = self.user.find_one({"_id": id})
        actual_user = User.User(user['name'], user['email'], user['password'], user['role'])
        return actual_user

    def find_user_by_email(self, emailAddress):
        user = self.user.find_one({'useremail': emailAddress})
        actual_user = User.User(user['name'], user['email'], user['password'], user['role'])
        return actual_user

    def find_user_by_hash(self, hash):
        user = self.user.find_one({'hash': hash})
        if user is not None:
            actual_user = User.User(user['name'], user['email'], user['password'], user['role'])
            return actual_user

    def insert_user(self, new_user):
        store_user = [{'name': new_user.name, 'email': new_user.email,
                        'password': new_user.password, 'role': new_user.role, 
                        'hash': new_user.email+new_user.password,
                        }]
        self.user.insert(store_user)
        
    def delete_all_users(self):
        self.user.remove()

    def convert_to_user(self, user):
        if user is not None:
            actual_user = User.User(user['name'], user['email'], user['password'], user['role'])
            return actual_user