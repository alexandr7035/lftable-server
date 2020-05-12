import src.static
import src.database

class Server():

    def __init__(self):
        self.timesdb = src.database.TimesDB()



    def get_timetable(self, timetable_name):
        return(timetable_name, 200)


