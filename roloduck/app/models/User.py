__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import hashlib

# Defined user roles
ROLE_USER = 0
ROLE_ADMIN = 1

# Defined company subscription types
COMPANY_TYPE_FREE = 0
COMPANY_TYPE_PRO = 1
COMPANY_TYPE_PREMIUM = 2

class User():

    def __init__(self, name, email, password, role, company):
        temp = password
        self.id =  self.hide_user_password(temp)
        self.name = name
        self.email = email
        # TODO hash this
        self.password = password
        self.role = role
        self.hash = email + password
        self.company = company

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def hash_sequence(self, email, password):
        sha = hashlib.sha1(email + password)
        return sha.hexdigest()

    def hide_user_password(self, password):
        md5 = hashlib.md5(password)
        return md5.hexdigest()

    # A helper method to create the partner dict
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
                'hash': self.hash
               }