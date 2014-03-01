__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.Project import Project
from app.db.RoloDuckDao import RoloDuckDao
from bson.objectid import ObjectId


class ProjectDao(RoloDuckDao):
    """
    Handles interactions with the database involving Projects
    """

    def __init__(self, database):
        """
        Connect to the proper database and collection
        """
        self.collection = database.project
        RoloDuckDao.__init__(self, database, self.collection)

    def find_project_by_id(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def find_project_by_client_id(self, client_id):
        return self.collection.find_one({'client_id': client_id})

    def find_project_by_created_by_user(self, created_by_user):
        return self.collection.find_one({'created_by_user': created_by_user})

    # A helper method to convert a projectDao model to an actual Project model
    def convert_to_project(self):
        actual_project = Project(self['project_name'],
                                 self['project_description'],
                                 self['client_id'],
                                 self['created_by_user'],
                                 self['date_created'])
        return actual_project