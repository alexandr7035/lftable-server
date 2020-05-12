import src.static
import src.database
import src.gettime
from flask import json
import os

class Server():

    def __init__(self):
        self.timetablesdb = src.database.TimetablesDB()

        # Create databases. See db_classes.py (especially 'construct()' methods)
        #TimesDS
        if not os.path.isfile(src.static.timetablesdb_path):
            self.timetablesdb.connect()
            self.timetablesdb.construct()
            self.timetablesdb.close()

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
       


