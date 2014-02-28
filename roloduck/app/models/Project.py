__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import time


class Project():

    def __init__(self, project_name, project_description, client_id, created_by_user):
        self.project_name = project_name
        self.project_description = project_description
        # Pass in the linked client id
        self.client_id = client_id
        # Store who created this Project
        self.created_by_user = created_by_user
        self.date_created = time.strftime("%c")

    def get_id(self):
        return unicode(self.id)

    def get_date_created(self):
        return self.date_created