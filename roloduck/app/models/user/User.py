__author__ = 'pjo336'

import hashlib

# Defined user roles
ROLE_USER = 0
ROLE_ADMIN = 1

class User():

    def __init__(self, name, email, password, role):
        temp = password
        self.id =  self.hide_user_password(temp)
        self.name = name
        self.email = email
        # TODO hash this
        self.password = password
        self.role = role
        self.hash = email + password

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