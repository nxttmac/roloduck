__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

from app.models.Project import Project
from bson.objectid import ObjectId


class ProjectDao(object):

    def __init__(self, database):
        self.db = database
        self.project = database.project

    def find_projects(self):
        list = []
        for each_project in self.project.find():
            list.append({'_id': each_project['_id'],
                         'project_name': each_project['project_name'],
                         'project_description': each_project['project_description'],
                         'client_id': each_project['client_id'],
                         'created_by_user': each_project['created_by_user'],
                         'date_created': each_project['date_created']
                         })
        return list

    def find_project_by_id(self, id):
        project = self.project.find_one({"_id": ObjectId(id)})
        return self.convert_to_project_dict(project)

    def find_project_by_client_id(self, client_id):
        project = self.project.find_one({'client_id': client_id})
        return self.convert_to_project_dict(project)

    def find_project_by_created_by_user(self, created_by_user):
        project = self.project.find_one({'created_by_user': created_by_user})
        return self.convert_to_project_dict(project)

    def insert_project(self, project):
        store_project = [{'project_name': project.project_name,
                         'project_description': project.project_description,
                         'client_id': project.client_id,
                         'created_by_user': project.created_by_user,
                         'date_created': project.date_created
                         }]
        self.project.insert(store_project)
        
    # A helper method to convert a projectDao model to an actual Project model
    def convert_to_project(self, project):
        if project is not None:
            actual_project = Project(project['project_name'], 
                                             project['project_description'],
                                             project['client_id'], 
                                             project['created_by_user'],
                                             project['date_created']
                                             )
            return actual_project

    # A helper method to create the project dict
    def convert_to_project_dict(self, project):
        return {'project_name': project['project_name'],
                         'project_description': project['project_description'],
                         'client_id': project['client_id'],
                         'created_by_user': project['created_by_user'],
                         'date_created': project['date_created']
                         }