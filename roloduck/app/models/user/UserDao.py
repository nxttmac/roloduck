class UserDao(object):

    def __init__(self, database):
        self.db = database
        self.user = database.user

    def find_users(self):
        l = []
        for each_user in self.user.find():
            l.append({'name':each_user['name'], 'email':each_user['email']})
        return l
        
    def insert_user(self, name, email):
        new_user = {'name':name, 'email':email}
        self.user.insert(new_user)
        
    def delete_all_users(self):
        self.user.remove()