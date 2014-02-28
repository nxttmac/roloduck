__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import time


class Partner():

    def __init__(self, partner_name, partner_description, client_id, created_by_user, contacts=None):
        self.partner_name = partner_name
        self.partner_description = partner_description
        # Pass in the linked client id
        self.client_id = client_id
        # Store who created this Project
        self.created_by_user = created_by_user
        self.date_created = time.strftime("%c")
        if contacts is None:
            self.contacts = []
        else:
            self.contacts = contacts

    def get_id(self):
        return unicode(self.id)

    def get_date_created(self):
        return self.date_created