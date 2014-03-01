__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import hashlib
from uuid import uuid1
from bson.objectid import ObjectId

# Defined user roles
ROLE_USER = 0
ROLE_ADMIN = 1

# Defined company subscription types
COMPANY_TYPE_FREE = 0
COMPANY_TYPE_PRO = 1
COMPANY_TYPE_PREMIUM = 2


class User():
    """
    Represents a User of the site including their login information
    """

    def __init__(self, name, email, password, role, company, login_hash=None):
        self.id = ObjectId()
        self.name = name
        self.email = email
        self.password = password
        self.role = role
        self.company = company
        if login_hash is None:
            self.login_hash = uuid1()
        else:
            self.login_hash = login_hash

    @staticmethod
    def is_authenticated():
        """
        Is the current user authenticated
        """
        return True

    @staticmethod
    def is_active():
        """
        Is the current user active
        """
        return True

    @staticmethod
    def is_anonymous():
        """
        Is the current user anonymous
        """
        return False

    def get_id(self):
        """
        Return the current users id
        """
        return unicode(self.id)

    def get_login_hash(self):
        """
        Return the current users login_hash
        """
        return self.login_hash

    @staticmethod
    def hide_user_password(password):
        """
        Hash the users password so it is stored encrypted
        """
        md5 = hashlib.md5(password)
        return md5.hexdigest()

    def get_user_map(self):
        """
        Return a JSON version of the current User. Used to store in a database
        Note: Anytime we add or remove a field from the User class, if we want the
        change reflected in the database, we'll have to change it here as well
        """
        return {'name': self.name,
                'email': self.email,
                'password': self.password,
                'role': self.role,
                'company': self.company,
                'login_hash': self.login_hash}