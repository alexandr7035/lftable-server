# Version number
lftable_server_version = '1.6'


# Pathes
db_dir = 'db/'
timetablesdb_path = db_dir + 'cached_timetables.db'
log_dir = 'log/'
log_file = log_dir + 'lftable.log'

db_date_format = '%d.%m.%Y %H:%M:%S'

# Intervals (s)
check_updates_interval = 120
max_request_delay = 5


# Class to store timetable options
class Timetable():
    pass


# All types of timetables for all courses
pravo_c1 = Timetable()
pravo_c2 = Timetable()
pravo_c3 = Timetable()
pravo_c4 = Timetable()
mag_c1 = Timetable()
mag_c2 = Timetable()
ek_polit_c1 = Timetable()
ek_polit_c2 = Timetable()
ek_polit_c3 = Timetable()
ek_polit_c4 = Timetable()

credit_c1 = Timetable()
exam_c1 = Timetable()
credit_c2 = Timetable()
exam_c2 = Timetable()
credit_c3 = Timetable()
exam_c3 = Timetable()
credit_c4 = Timetable()
exam_c4 = Timetable()


# List to simplify 'for' loops
all_timetables = [pravo_c1, pravo_c2, pravo_c3, pravo_c4, 
                 ek_polit_c1, ek_polit_c2, ek_polit_c3, ek_polit_c4,
                 mag_c1, mag_c2,
                 credit_c1, credit_c2, credit_c3, credit_c4, 
                 exam_c1, exam_c2, exam_c3, exam_c4]

# List for only credits and exams 
credit_exam_timetables = [credit_c1, exam_c1, credit_c2, exam_c2,
                              credit_c3, exam_c3, credit_c4, exam_c4]


# Timetable data
pravo_c1.url = 'https://law.bsu.by/pub/2/Raspisanie_1_pravo.xls'
pravo_c1.shortname = 'pravo_c1'

pravo_c2.url = 'https://law.bsu.by/pub/2/Raspisanie_2_pravo.xls'
pravo_c2.shortname = 'pravo_c2'

pravo_c3.url = 'https://law.bsu.by/pub/2/Raspisanie_3_pravo.xls'
pravo_c3.shortname = 'pravo_c3'

pravo_c4.url = 'https://law.bsu.by/pub/2/Raspisanie_4_pravo.xls'
pravo_c4.shortname = 'pravo_c4'

ek_polit_c1.url = 'https://law.bsu.by/pub/2/Raspisanie_1_ek_polit.xls'
ek_polit_c1.shortname = 'ek_polit_c1'

ek_polit_c2.url = 'https://law.bsu.by/pub/2/Raspisanie_2_ek_polit.xls'
ek_polit_c2.shortname = 'ek_polit_c2'

ek_polit_c3.url = 'https://law.bsu.by/pub/2/Raspisanie_3_ek_polit.xls'
ek_polit_c3.shortname = 'ek_polit_c3'

ek_polit_c4.url = 'https://law.bsu.by/pub/2/Raspisanie_4_ek_polit.xls'
ek_polit_c4.shortname = 'ek_polit_c4'

mag_c1.url = 'https://law.bsu.by/pub/2/Raspisanie_mag_1_kurs_1s.xlsx'
mag_c1.shortname = 'mag_c1'

mag_c2.url = 'https://law.bsu.by/pub/2/Raspisanie_mag_2_kurs.xls'
mag_c2.shortname = 'mag_c2'


# This part is for credits and exams
# The complication caused by division into summer and 
# winter exam/credit timetable files on the site
credit_c1.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_zachet_1k.xls',
                  'summer' : 'https://law.bsu.by/pub/2/leto_zachet_1k.xls'}
credit_c1.shortname = 'credit_c1'

exam_c1.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_ekz_1k.xls',
                  'summer' : 'https://law.bsu.by/pub/2/leto_ekz_1k.xls'}
exam_c1.shortname = 'exam_c1'

credit_c2.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_zachet_2k.xls',
                  'summer' : 'https://law.bsu.by/pub/2/leto_zachet_2k.xls'}
credit_c2.shortname = 'credit_c2'

exam_c2.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_ekz_2k.xls',
                  'summer' : 'https://law.bsu.by/pub/2/leto_ekz_2k.xls'}
exam_c2.shortname = 'exam_c2'

credit_c3.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_zachet_3k.xls',
                  'summer' : 'https://law.bsu.by/pub/2/leto_zachet_3k.xls'}
credit_c3.shortname = 'credit_c3'

exam_c3.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_ekz_3k.xls',
                  'summer' : 'https://law.bsu.by/pub/2/leto_ekz_3k.xls'}
exam_c3.shortname = 'exam_c3'


# Only winter timetable avaliable for course 4
credit_c4.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_zachet_4k.xls'}
credit_c4.shortname = 'credit_c4'

exam_c4.urls = {'winter' : 'https://law.bsu.by/pub/2/zima_ekz_4k.xls'}
exam_c4.shortname = 'exam_c4'





