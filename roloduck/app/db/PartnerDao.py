__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.Partner import Partner
from bson.objectid import ObjectId


class PartnerDao(object):

    def __init__(self, database):
        self.db = database
        self.partner = database.partner

    def find_partners(self):
        list = []
        for each_partner in self.partner.find():
            list.append({'_id': each_partner['_id'],
                         'partner_name': each_partner['partner_name'],
                         'partner_description': each_partner['partner_description'],
                         'client_id': each_partner['client_id'],
                         'created_by_user': each_partner['created_by_user'],
                         'date_created': each_partner['date_created']
                         })
        return list

    def find_partner_by_id(self, id):
        partner = self.partner.find_one({"_id": ObjectId(id)})
        return self.convert_to_partner_dict(partner)

    def find_partner_by_client_id(self, client_id):
        partner = self.partner.find_one({'client_id': client_id})
        return self.convert_to_partner_dict(partner)

    def find_partner_by_created_by_user(self, created_by_user):
        partner = self.partner.find_one({'created_by_user': created_by_user})
        return self.convert_to_partner_dict(partner)

    def insert_partner(self, partner):
        store_partner = [{'partner_name': partner.partner_name,
                         'partner_description': partner.partner_description,
                         'client_id': partner.client_id,
                         'created_by_user': partner.created_by_user,
                         'date_created': partner.date_created,
                         'contacts': partner.contacts
                         }]
        self.partner.insert(store_partner)

    # A helper method to convert a partnerDao model to an actual partner model
    def convert_to_partner(self, partner):
        if partner is not None:
            actual_partner = Partner(partner['partner_name'], 
                                             partner['partner_description'],
                                             partner['client_id'], 
                                             partner['created_by_user'],
                                             partner['date_created']
                                             )
            return actual_partner

    # A helper method to create the partner dict
    def convert_to_partner_dict(self, partner):
        return {'partner_name': partner['partner_name'],
                         'partner_description': partner['partner_description'],
                         'client_id': partner['client_id'],
                         'created_by_user': partner['created_by_user'],
                         'date_created': partner['date_created']
                         }