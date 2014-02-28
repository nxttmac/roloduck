__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014

import time


class Project():
    """
    Represents a Project
    """

    def __init__(self, project_name, project_description, client_id, created_by_user):
        self.project_name = project_name
        self.project_description = project_description
        # Pass in the linked client id
        self.client_id = client_id
        # Store who created this Project
        self.created_by_user = created_by_user
        self.date_created = time.strftime("%c")

    def get_id(self):
        """
        Return the id of the current Project
        """
        return unicode(self.id)

    def get_date_created(self):
        """
        Return the date the current Project was created
        """
        return self.date_created

    def get_project_map(self):
        """
        Return a JSON version of the current Project. Used to store in a database
        Note: Anytime we add or remove a field from the Project class, if we want the
        change reflected in the database, we'll have to change it here as well
        """
        return {'project_name': self.project_name,
                'project_description': self.project_description,
                'client_id': self.client_id,
                'created_by_user': self.created_by_user,
                'date_created': self.date_created
                }