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
        return self.collection.find_one({"_id": ObjectId(id)})

    def find_user_by_email(self, email_address):
        """
        Find the user with the given email
        """
        return self.collection.find_one({'email': email_address})

    def find_user_by_hash(self, hash):
        """
        Find the user with the given hash
        """
        try:
            return self.collection.find_one({'login_hash': hash})
        except KeyError:
            # TODO Do something with the error
            print 'Key Error bro!'

    def convert_to_user(self):
        """
        Convert the object to a real user
        """
        # TODO we need to work on the user constructor to deal with this method
        return User(self['name'], self['email'], self['password'], self['role'],
                    self['company'], self['login_hash'])