from app.models.user import User

class UserDao(object):

    def __init__(self, database):
        self.db = database
        self.user = database.user

    def find_users(self):
        list = []
        for each_user in self.user.find():
            list.append({'firstname': each_user['firstname'],
                         'lastname': each_user['lastname'],
                         'useremail': each_user['useremail']})
        return list

    def find_user_by_id(self, id):
        self.user.find_one({"_id": id})

    def find_user_by_email(self, emailAddress):
        self.user.find_one({'useremail': emailAddress})

    def insert_user(self, new_user):
        self.user.insert(new_user)
        
    def delete_all_users(self):
        self.user.remove()