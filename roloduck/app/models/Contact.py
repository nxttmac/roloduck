__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import time


class Contact():
    """
    This class represents a Contact object that belongs to a Partner
    """

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
        """
        Return the id of the current Contact
        """
        return unicode(self.id)

    def get_date_created(self):
        """
        Return the date the current Contact was created
        """
        return self.date_created

    def get_contact_map(self):
        """
        Return a JSON version of the current Contact. Used to store in a database
        Note: Anytime we add or remove a field from the Contact class, if we want the
        change reflected in the database, we'll have to change it here as well
        """
        return {'contact_first_name': self.contact_first_name,
                'contact_last_name': self.contact_last_name,
                'contact_role': self.contact_role,
                'contact_title': self.contact_title,
                'contact_email': self.contact_email,
                'contact_phone': self.contact_phone,
                'client_id': self.client_id,
                'created_by_user': self.created_by_user,
                'date_created': self.date_created
                }