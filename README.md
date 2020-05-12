### DESKRIPTION

***lftable-server*** is a simple api for telegram and vk lftable clients.
Based on flask. Docker and docker-compose are used to run the app.

### ROUTES:

    /timetable?timetable_mame=<TIMETABLE_NAME>

**Returns the following json**

    timetable_data = {  
    	"short_name" : timetable.shortname,  
            "full_mame": timetable.name,  
            "update_time": update_time,  
            "relevant_url" : relevant_url  
    }



**TIMETABLE_NAME** here must be from this list:

     - pravo_c1,  pravo_c2, pravo_c3, pravo_c4
     - ek_polit_c1, ek_polit_c2, ek_polit_c3, ek_polit_c4
     - mag_c1, mag_c2
     - credit_c1, credit_c2, credit_c3, credit_c4
     - exam_c1, exam_c2, exam_c3, exam_c4

### REQUIREMENTS

See requirements.txt

### NSTALLATION AND LAUNCH:

    # sudo docker-compose up --build

### CREATED FILES

 - log/ directory contains lftable.log file
 - db/ direcory contains cached_timtables.db database file


