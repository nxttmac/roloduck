__author__ = 'Andrew Ertell'
__author__ = 'Peter Johnston'
# Roloduck 2014


class RoloDuckDao(object):
    """
    This class is the main abstract Dao which every other Dao will extend.
    It will provide most basic CRUD operations
    """
    def __init__(self, database, collection):
        """
        Connect to the proper database and the proper collection
        """
        self.db = database
        self.collection = collection

    def insert_obj(self, obj):
        """
        Add the given object to the database
        Return the id
        """
        return self.collection.insert(obj)

    def find_all(self):
        """
        Find all objects stored in the collection
        """
        obj_list = []
        for each_obj in self.collection.find():
            if each_obj is not None:
                obj_list.append(each_obj)
        return obj_list

    def remove_all(self):
        """
        Remove all objects from the collection
        """
        self.collection.remove()