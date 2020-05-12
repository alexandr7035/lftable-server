import sqlite3
import src.static


# Base db class 
class CommonDB():
    # Used to set the path to a database
    def __init__(self, db_path):
        self.db_path = db_path

    # Connects to the databas
    # Also creates an empty base if there is still no 'db_path' base
    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    # Closes the db
    def close(self):
        self.connection.commit()
        self.connection.close()


# Stores update time of each timetable
class TimetablesDB(CommonDB):
    def __init__(self):
        # Set path to the db
        super().__init__(src.static.timetablesdb_path)

    # Creates necessary tables after db was created
    def construct(self):
        self.cursor.execute('CREATE TABLE cached_timetables (timetable, update_time, relevant_url)')

        for timetable in src.static.all_timetables:
            self.cursor.execute('INSERT INTO cached_timetables VALUES ("' + timetable.shortname + '", "", "")')

        self.connection.commit()

    # Get timetable's update time written before
    def get_time(self, timetable_name):
        self.cursor.execute("SELECT update_time FROM cached_timetables WHERE (timetable = ?)", (timetable_name,))
        time = self.cursor.fetchall()[0][0]
        return(time)

    # Write a new update time to the db
    def write_time(self, timetable_name, update_time):
        self.cursor.execute("UPDATE cached_timetables SET update_time = '" + update_time + "' WHERE (timetable = ?)", (timetable_name,))
        self.connection.commit()

    # Get timetable's relevant url
    def get_url(self, timetable_name):
        self.cursor.execute("SELECT relevant_url FROM cached_timetables WHERE (timetable = ?)", (timetable_name,))
        url = self.cursor.fetchall()[0][0]
        return(url)

    # Update timetable's relevant url
    def write_url(self, timetable_name, timetable_url):
        self.cursor.execute("UPDATE cached_timetables SET relevant_url = '" + timetable_url + "' WHERE (timetable = ?)", (timetable_name,))
        self.connection.commit()


