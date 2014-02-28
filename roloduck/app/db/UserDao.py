__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.db.RoloDuckDao import RoloDuckDao
from app.models.User import User
from bson.objectid import ObjectId


class UserDao(RoloDuckDao):
    """
    Handles interactions with the database involving Users
    """

    def __init__(self, database):
        """
        Connect to the proper database and collection
        """
        self.collection = database.user
        RoloDuckDao.__init__(self, database, self.collection)

    def find_user_by_id(self, id):
        """
        Find the user with the given id
        """
        user = self.collection.find_one({"_id": ObjectId(id)})
        return self.convert_to_user(user)

    def find_user_by_email(self, emailAddress):
        """
        Find the user with the given email
        """
        user = self.collection.find_one({'useremail': emailAddress})
        return self.convert_to_user(user)

    def find_user_by_hash(self, hash):
        """
        Find the user with the given hash
        """
        try:
            user = self.collection.find_one({'hash': hash})
            return self.convert_to_user(user)
        except KeyError:
            # TODO Do something with the error
            print 'Key Error bro!'

    def convert_to_user(self, user):
        """
        Convert the object to a real user
        """
        # TODO we need to work on the user constructor to deal with this method
        if user is not None:
            actual_user = User(user['name'], user['email'], user['password'], user['role'], user['company'])
            return actual_user