__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.contact import Contact
from bson.objectid import ObjectId


class ContactDao(object):

    def __init__(self, database):
        self.db = database
        self.contact = database.contact

    def find_contacts(self):
        list = []
        for each_contact in self.contact.find():
            list.append({'_id': each_contact['_id'],
                         'contact_firstName': each_contact['contact_firstName'],
                         'contact_lastName': each_contact['contact_lastName'],
                         'contact_role': each_contact['contact_role'],
                         'contact_title': each_contact['contact_title'],
                         'contact_email': each_contact['contact_email'],
                         'contact_phone': each_contact['contact_phone'],
                         'client_id': each_contact['client_id'],
                         'created_by_user': each_contact['created_by_user'],
                         'date_created': each_contact['date_created']
                         })
        return list

    def find_contact_by_id(self, id):
        contact = self.contact.find_one({"_id": ObjectId(id)})
        return self.convert_to_contact_dict(contact)

    def find_contact_by_client_id(self, client_id):
        contact = self.contact.find_one({'client_id': client_id})
        return self.convert_to_contact_dict(contact)

    def find_contact_by_created_by_user(self, created_by_user):
        contact = self.contact.find_one({'created_by_user': created_by_user})
        return self.convert_to_contact_dict(contact)

    def insert_contact(self, contact):
        store_contact = [{'contact_firstName': contact.contact_firstName,
                         'contact_lastName': contact.contact_lastName,
                         'contact_role': contact.contact_role,
                         'contact_title': contact.contact_title,
                         'contact_email': contact.contact_email,
                         'contact_phone': contact.contact_phone,
                         'client_id': contact.client_id,
                         'created_by_user': contact.created_by_user,
                         'date_created': contact.date_created
                         }]
        self.contact.insert(store_contact)
        
    def delete_all_contacts(self):
        self.contact.remove()

    # A helper method to convert a contactDao model to an actual Contact model
    def convert_to_contact(self, contact):
        if contact is not None:
            actual_contact = Contact.Contact(contact['contact_firstName'], 
                                             contact['contact_lastName'],
                                             contact['contact_role'],
                                             contact['contact_title'],
                                             contact['contact_email'],
                                             contact['contact_phone'],
                                             contact['client_id'], 
                                             contact['created_by_user'],
                                             contact['date_created']
                                             )
            return actual_contact

    # A helper method to create the contact dict
    def convert_to_contact_dict(self, contact):
        return {'contact_firstName': contact['contact_firstName'],
                         'contact_lastName': contact['contact_lastName'],
                         'contact_role': contact['contact_role'],
                         'contact_title': contact['contact_title'],
                         'contact_email': contact['contact_email'],
                         'contact_phone': contact['contact_phone'],
                         'client_id': contact['client_id'],
                         'created_by_user': contact['created_by_user'],
                         'date_created': contact['date_created']
                         }