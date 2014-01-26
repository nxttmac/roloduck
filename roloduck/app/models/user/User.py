__author__ = 'pjo336'

# Defined user roles
ROLE_USER = 0
ROLE_ADMIN = 1

class User():

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)