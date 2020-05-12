from flask import Flask, request
import src.static
import src.server


app = Flask(__name__)

server = src.server.Server()

# List of possible timetable codes
possible_timetables = []
for timetable in src.static.all_timetables:
    possible_timetables.append(timetable.shortname)

@app.route('/timetable', methods=['GET'])
def get_timetable():

    requested_timetable = request.args.get('timetable_name')

    if requested_timetable in possible_timetables:
        return(server.get_timetable(requested_timetable))
    else:
        return('Invalid timetable name. Possible variants are: ' + str(possible_timetables))


app.run(debug=True)