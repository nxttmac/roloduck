__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.Partner import Partner
from app.db.RoloDuckDao import RoloDuckDao
from bson.objectid import ObjectId


class PartnerDao(RoloDuckDao):

    def __init__(self, database):
        self.collection = database.partner
        RoloDuckDao.__init__(self, database, self.collection)

    def find_partner_by_id(self, id):
        partner = self.collection.find_one({"_id": ObjectId(id)})
        return self.convert_to_partner_dict(partner)

    def find_partner_by_client_id(self, client_id):
        partner = self.collection.find_one({'client_id': client_id})
        return self.convert_to_partner_dict(partner)

    def find_partner_by_created_by_user(self, created_by_user):
        partner = self.collection.find_one({'created_by_user': created_by_user})
        return self.convert_to_partner_dict(partner)

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