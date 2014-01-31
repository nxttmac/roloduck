__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# ©Roloduck 2014

from app.models.user import User
class UserDao(object):

    def __init__(self, database):
        self.db = database
        self.user = database.user

    def find_users(self):
        list = []
        for each_user in self.user.find():
            list.append({'name': each_user['name'],
                         'role': each_user['role'],
                         'email': each_user['email'],
                         'password': each_user['password'],
                         'hash': each_user['hash'],
                         'company': each_user['company']
                         })
        return list

    def find_user_by_id(self, id):
        user = self.user.find_one({"_id": id})
        return self.convert_to_user(user)

    def find_user_by_email(self, emailAddress):
        user = self.user.find_one({'useremail': emailAddress})
        return self.convert_to_user(user)

    def find_user_by_hash(self, hash):
        user = self.user.find_one({'hash': hash})
        return self.convert_to_user(user)

    def insert_user(self, new_user):
        store_user = [{'name': new_user.name, 'email': new_user.email,
                        'password': new_user.password, 'role': new_user.role, 
                        'hash': new_user.email+new_user.password,
                        'company': new_user.company
                        }]
        self.user.insert(store_user)
        
    def delete_all_users(self):
        self.user.remove()

    def convert_to_user(self, user):
        if user is not None:
            actual_user = User.User(user['name'], user['email'], user['password'], user['role'], user['company'])
            return actual_user