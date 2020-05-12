from flask import Flask, request
import src.static

app = Flask(__name__)


@app.route('/timetable', methods=['GET'])
def get_timetable():

    requested_timetable = request.args.get('timetable_name')

    if requested_timetable in possible_timetables:
        return(requested_timetable, 200)
    else:
        return('Timetable code is incorrect. Possible variants: ' + str(possible_timetables), 200)


if __name__ == '__main__':
    
    # List of possible timetable codes
    possible_timetables = []
    for timetable in src.static.all_timetables:
        possible_timetables.append(timetable.shortname)

    app.run(debug=True, port=5000)