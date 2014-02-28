__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.db.RoloDuckDao import RoloDuckDao
from app.models.User import User
from bson.objectid import ObjectId


class UserDao(RoloDuckDao):

    def __init__(self, database):
        self.collection = database.user
        RoloDuckDao.__init__(self, database, self.collection)

    def find_user_by_id(self, id):
        user = self.collection.find_one({"_id": ObjectId(id)})
        return self.convert_to_user(user)

    def find_user_by_email(self, emailAddress):
        user = self.collection.find_one({'useremail': emailAddress})
        return self.convert_to_user(user)

    def find_user_by_hash(self, hash):
        try:
            user = self.collection.find_one({'hash': hash})
            return self.convert_to_user(user)
        except KeyError:
            # TODO Do something with the error
            print 'Key Error bro!'

    def convert_to_user(self, user):
        if user is not None:
            actual_user = User(user['name'], user['email'], user['password'], user['role'], user['company'])
            return actual_user