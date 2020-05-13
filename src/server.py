import os
import time
import atexit
from datetime import datetime

import src.static
import src.database
import src.gettime
from src.logger import *

from flask import json
from apscheduler.schedulers.background import BackgroundScheduler


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

        try:
            for timetable in src.static.all_timetables:
                if timetable in src.static.credit_exam_timetables:
                    data = src.gettime.credit_exam_gettime(timetable)
                    update_time = data['time']
                    relevant_url = data['url']
                else:
                    update_time = src.gettime.gettime(timetable)
                    relevant_url = timetable.url

                self.timetablesdb.write_time(timetable.shortname, update_time.strftime(src.static.db_date_format))
                self.timetablesdb.write_url(timetable.shortname, relevant_url)
        
        except Exception:
            logger.critical("can't get data from law.bsu.by on start. EXIT")
            exit()

        self.timetablesdb.close()


        # Start the updates_timejob
        # Checks for updates (see src.static.check_updates_interval variable)
        # Writes relevant times and urls to the db
        #
        # Used 'atexit' to shut down the scheduler when exiting the app
        scheduler = BackgroundScheduler()
        scheduler.add_job(func=self.updates_timejob,
                          trigger="interval",
                          seconds=src.static.check_updates_interval)
        scheduler.start()
        atexit.register(lambda: scheduler.shutdown())
            

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
            "update_time": update_time,
            "relevant_url" : relevant_url
        }

        return(json.dumps(timetable_data, ensure_ascii=False).encode("utf-8"))


    # Called periodically 
    # See src.static.check_updates_interval variable
    # Updates times and urls in the cache (database)
    def updates_timejob(self):
        print('Checking for timetables\' updates was started at ', datetime.now().strftime("%d.%m.%Y %Y %H:%M:%S"))

        # Connect to the times.db
        self.timetablesdb.connect()

        # See 'all_timetables' list in 'src/static.py'
        for timetable in src.static.all_timetables:

            # Get timetable update time from law.bsu.by
            # Use different gettime functions for ussual and credit/exam timetables. See src.gettime.py
            try:

                if timetable in src.static.credit_exam_timetables:
                    data = src.gettime.credit_exam_gettime(timetable)
                    update_time = data['time'].strftime(src.static.db_date_format)
                    relevant_url = data['url']
                else:
                    update_time = src.gettime.gettime(timetable).strftime(src.static.db_date_format)
                    relevant_url = timetable.url

            # Exit function if fails here
            # (Until next check)
            except Exception:
                logger.critical("can't get data from law.bsu.by. Left cache as is")
                return


            # Get old update time from the TimesDB.
            old_update_time = self.timetablesdb.get_time(timetable.shortname)

            # Convert date strings to datetime objects
            dt_update_time = datetime.strptime(update_time, '%d.%m.%Y %H:%M:%S')
            dt_old_update_time = datetime.strptime(old_update_time, '%d.%m.%Y %H:%M:%S')

            # Compare the two dates
            # If timetable was updated send a notification to users who enabled notifications for this timetable
            if dt_update_time > dt_old_update_time:

                logger.info("'" + timetable.shortname + "' timetable was updated at " + update_time)
                # Write new update time to the database.
                self.timetablesdb.write_time(timetable.shortname, update_time)


            # Compare 2 urls
            # Update if changed
            if self.timetablesdb.get_url(timetable.shortname) != relevant_url:
                logger.info("'" + timetable.shortname + "': url updated at " + update_time)
                # Write new url to the database
                self.timetablesdb.write_url(timetable.shortname, relevant_url)


        # Close 'times.db' until next check.
        self.timetablesdb.close()   


