__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.Partner import Partner
from app.db.RoloDuckDao import RoloDuckDao
from bson.objectid import ObjectId


class PartnerDao(RoloDuckDao):
    """
    Handles interactions with the database involving Partners and its Contacts
    """

    def __init__(self, database):
        """
        Connect to the database and the proper collection
        """
        self.collection = database.partner
        RoloDuckDao.__init__(self, database, self.collection)

    def find_partner_by_id(self, id):
        """
        Find the partner with the given id
        """
        return self.collection.find_one({"_id": ObjectId(id)})

    def find_partner_by_client_id(self, client_id):
        """
        Find the partner with the given client_id
        """
        return self.collection.find_one({'client_id': client_id})

    def find_partner_by_created_by_user(self, created_by_user):
        """
        Find the partner created by the given user
        """
        return self.collection.find_one({'created_by_user': created_by_user})

    def add_contact_to_partner(self, partner_id, partner):
        """
        Add the contact to the partners contacts list
        """
        self.collection.update({'_id': ObjectId(partner_id)},
                               {'$set': {'contacts': partner.contacts}})

    # A helper method to convert a partnerDao model to an actual partner model
    def convert_to_partner(self):
        actual_partner = Partner(self['partner_name'],
                                 self['partner_description'],
                                 self['client_id'],
                                 self['created_by_user'],
                                 self['date_created'])
        return actual_partner