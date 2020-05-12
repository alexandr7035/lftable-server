import src.static
import src.database
import src.gettime
from flask import json
import os

from src.logger import *

class Server():

    def __init__(self):

        logger.info("-")
        logger.info("the app has been STARTED now")

        # DB object for the app
        self.timetablesdb = src.database.TimetablesDB()

        # Create directory for databases if still not created
        if not os.path.exists(src.static.db_dir):
            os.mkdir(src.static.db_dir)
            logger.info("'" + src.static.db_dir + "' directory was created")

        # Create databases if don't exist. 
        # See db_classes.py (especially 'construct()' methods)
        if not os.path.isfile(src.static.timetablesdb_path):
            self.timetablesdb.connect()
            self.timetablesdb.construct()
            self.timetablesdb.close()

            logger.info("'" + src.static.timetablesdb_path + "' database was created")

        
        # Set actual updates' times to the db on start
        # To prevent late notifications
        self.timetablesdb.connect()
        for timetable in src.static.all_timetables:
            if timetable in src.static.credit_exam_timetables:
                data = src.gettime.credit_exam_gettime(timetable)
                update_time = data['time']
                relevant_url = data['url']
            else:
                update_time = src.gettime.gettime(timetable)
                relevant_url = timetable.url

            relevant_url = str(relevant_url)

            self.timetablesdb.write_time(timetable.shortname, update_time.strftime(src.static.db_date_format))
            self.timetablesdb.write_url(timetable.shortname, relevant_url)

        self.timetablesdb.close()
            

    # !!!!!
    # The main method called by clients
    # Returns JSON with timetables info
    def get_timetable(self, timetable_name):
        
        # Get timetable object by it's name
        timetable = getattr(src.static, timetable_name)

        # Get values from cache
        self.timetablesdb.connect()
        update_time = self.timetablesdb.get_time(timetable.shortname)
        relevant_url = self.timetablesdb.get_url(timetable.shortname)
        self.timetablesdb.close()

        timetable_data = {
            "short_name" : timetable.shortname,
            "full_mame": timetable.name,
            "update_time": update_time,
            "relevant_url" : relevant_url
        }

        return(json.dumps(timetable_data, ensure_ascii=False).encode("utf-8"))
       


