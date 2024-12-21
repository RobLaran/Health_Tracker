Project #5 Health Tracker:

About:
    this project tracks user's health on such activity by logging, adding, or setting particular data related to health goals on their daily basis.
Features includes tracking calorie intake, track your body measurement, logging exercise routine, monitoring water intake and estimating your bed time sleep. Data will be saved into the json file for permanent storage, so we can reload the saved data into the program. It has some session to temporarily keep the user logged in.


# TODO
    - fix view logs in log water intake when first logging in
    - do some test with the new created features
        - test feature: log body measurement
        - test feature: log water intake
    - create feature: logging bed time sleep
    - create feature: logging exercise routine

# DONE
    2024.12.18
    - body measurement feature

    2024.12.20
    = logging water intake
        - work on viewing logs
        # output 
            display table form
            summary of total water intake, average, and set goal
    - fixed where to put the checkGoal() function
    
    2024.12.21
    - secured password(convert into hash)
    - fixed empty form in user registration

    
CLI-Based Design:

* Standby
<!-- - tracking calorie intake functionalities:
    # user inputs calories
    # add it into the database
    # calculates the calories into total and average calories(this week or last week)

    data model:
        # date
        # calories -->

- add bed time sleep:
    # user inputs a bed time 
    # add it into the database
    # calculates the average and total

    data model:
        # date
        # day
        # hours_of_sleep

- monitoring water intake
    # user inputs water intake
    # add into the database
    # calculates the total and average

    data model:
        # date
        # water_intake
        # water_intake goal

- exercise routine
    # user selects or add some exercise and inputs the estimated time of exercise
    # add it into the database
    # calculates the total and average 
    
    data model:
        # date
        # calories_burned

- body measruement
    # user inputs weight in kg and height in cm
    # add it into the database
    # calculates the current data and average data and bmi

    data model:
        # date
        # weight
        # height

