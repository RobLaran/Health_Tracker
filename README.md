# Project #5 Health Tracker:

About:
    This project tracks user's health on such activity by logging, adding, or setting particular data related to health goals on their daily basis. Features includes tracking calorie intake, track your body measurement, logging exercise routine, monitoring water intake and estimating your bed time sleep. Data will be saved into the json file for permanent storage, so we can reload the saved data into the program. It has some session to temporarily keep the user logged in.

# TODO
    

# DONE
    2024.12.18
    - body measurement feature

    2024.12.20
    = logging water intake
        - work on viewing logs
        - output 
            display table form
            summary of total water intake, average, and set goal
    - fixed where to put the checkGoal() function
    
    2024.12.21
    - secured password(convert into hash)
    - fixed empty form in user registration

    2024.12.22
    - fixed view logs in log water intake when first logging in
    - stripped input value when there is a leading or trailing whitespaces

    2024.12.26
    - created feature: logging bed time sleep
    - created feature: logging exercise routine
        *   add data: date, type of activity, duration in hrs and mins, and calories burned
        *   view logs: a table format consisting all data, an average of burned calories, and a list of activities  added

    2024.12.28
    - added view summary option in main menu: summary option shows all the summary of data
        * calculate the monthly average weight
        * calculate the monthly average height
        * calculate the monthly average time slept
        * calculate the monthly average calories burned
        * calculate the monthly total calories burned
        * calculate the monthly total water intake

    
# CLI-Based Design:
    data model:
        - date
        - calories -->
    - user inputs a bed time 
    - add it into the database
    - calculates the average and total

    data model:
        - date
        - day
        - hours_of_sleep
    - user inputs water intake
    - add into the database
    - calculates the total and average

    data model:
        - date
        - water_intake
        - water_intake goal
    - user selects or add some exercise and inputs the estimated time of exercise
    - add it into the database
    - calculates the total and average 
    
    data model:
        - date
        - calories_burned
    - user inputs weight in kg and height in cm
    - add it into the database
    - calculates the current data and average data and bmi

    data model:
        - date
        - weight
        - height

