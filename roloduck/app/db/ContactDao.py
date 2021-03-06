__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.Contact import Contact
from app.db.RoloDuckDao import RoloDuckDao
from bson.objectid import ObjectId


class ContactDao(RoloDuckDao):
    """
    Handles interactions with the database involving a Contact
    """

    def __init__(self, database):
        self.collection = database.contact
        RoloDuckDao.__init__(self, database, self.collection)

    def find_contact_by_id(self, id):
        contact = self.contact.find_one({"_id": ObjectId(id)})
        return self.convert_to_contact_dict(contact)

    def find_contact_by_client_id(self, client_id):
        contact = self.contact.find_one({'client_id': client_id})
        return self.convert_to_contact_dict(contact)

    def find_contact_by_created_by_user(self, created_by_user):
        contact = self.contact.find_one({'created_by_user': created_by_user})
        return self.convert_to_contact_dict(contact)

    # A helper method to convert a contactDao model to an actual Contact model
    def convert_to_contact(self, contact):
        if contact is not None:
            actual_contact = Contact(contact['contact_name'], 
                                             contact['contact_description'],
                                             contact['client_id'], 
                                             contact['created_by_user'],
                                             contact['date_created']
                                             )
            return actual_contact