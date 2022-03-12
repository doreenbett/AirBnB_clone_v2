#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
-- Creates a MySQL server with:
	--   Database hbnb_test_db.
	  --   User hbnb_test with password hbnb_test_pwd in localhost.
	  --   Grants all privileges for hbnb_test on hbnb_test_db.
	  --   Grants SELECT privilege for hbnb_test on performance_schema.
	  
	  CREATE DATABASE IF NOT EXISTS hbnb_test_db;
	  CREATE USER
	      IF NOT EXISTS 'hbnb_test'@'localhost'
	          IDENTIFIED BY 'hbnb_test_pwd';
		  GRANT ALL PRIVILEGES
		     ON `hbnb_test_db`.*
		        TO 'hbnb_test'@'localhost'
			   IDENTIFIED BY 'hbnb_test_pwd';
			   GRANT SELECT
			      ON `performance_schema`.*
			         TO 'hbnb_test'@'localhost'
				    IDENTIFIED BY 'hbnb_test_pwd';
				    FLUSH PRIVILEGES;__file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)
									     
    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass
