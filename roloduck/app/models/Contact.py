__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import time


class Contact():

    def __init__(self, contact_first_name, contact_last_name,
                 contact_role, contact_title, contact_email, 
                 contact_phone, client_id, created_by_user):
        self.contact_first_name = contact_first_name
        self.contact_last_name = contact_last_name
        self.contact_role = contact_role
        self.contact_title = contact_title
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        # Pass in the linked client id
        self.client_id = client_id
        # Store who created this Contact
        self.created_by_user = created_by_user
        self.date_created = time.strftime("%c")

    def get_id(self):
        return unicode(self.id)

    def get_date_created(self):
        return self.date_created