from datetime import datetime
import os
import ast
from activity_class import Activity

def main():
    want_to_continue = True
    
    while want_to_continue:
        # Separator for less clutter
        print(50*"-")
        try:
            # Prompt user for input
            choice = int(input("""Please select from the following:
              1 - create a new activity
              2 - open an existing activity
              3 - exit application\n"""))
        except ValueError:
            # If user doesn't enter a number
            print("Please enter 1, 2, or 3")
        else:
            # If user enters a number that isn't 1, 2, or 3
            if choice not in (1, 2, 3):
                print("Please enter 1, 2, or 3")
                continue
            # User wants to create a new activity
            if choice == 1:
                date_time_location = get_date_time_location()
                if date_time_location == 'q': continue
                act = Activity(date_time_location, False)
            # User wants to access an exisiting activity
            elif choice == 2: 
                activity_data = get_past_activity()
                if activity_data == 'q': continue
                act = Activity(activity_data, True)
            # User wants to exit
            else:
                print('Goodbye')
                want_to_continue = False

def get_past_activity():
    past_activity_directory = os.path.join('.','activity_log')
    if not os.path.exists(past_activity_directory):
        os.mkdir(past_activity_directory)
    past_activities = os.listdir(past_activity_directory)
    input_not_valid = True
    while input_not_valid:
        print(50*'-')
        print('0 - exit past activities')
        for index, activity in enumerate(past_activities):
            print(f'{index + 1} - {activity}')
        try: choice = int(input('Please enter the number preceding the selected activity or press 0 to exit: '))
        except ValueError: print('Please enter a number.')
        else:
            if choice == 0:
                return 'q'
            if choice > len(past_activities):
                print('Invalid number.')
            else:
                selected_past_activity = os.path.join(past_activity_directory, past_activities[choice - 1])
                with open(selected_past_activity, 'r', encoding='utf-8') as f:
                    activity_data = f.read()
                return ast.literal_eval(activity_data)
        
def get_date_time_location():
    activity_data = {}
    # get date
    date_is_valid = False
    while date_is_valid == False:
        date_is_valid = Activity.validate_date(input('Please enter activity date (mm/dd/yyyy) or press q to exit: '))
        if date_is_valid == 'q': return 'q'
    # get time
    datetime_is_valid = False
    while datetime_is_valid == False:
        datetime_is_valid = Activity.validate_time(input('Please enter activity time (hh:mm) or press q to exit: '), date_is_valid)
        if datetime_is_valid == 'q': return 'q'
        if datetime_is_valid: activity_data['date and time'] = datetime_is_valid
    # get location
    location_is_valid = False
    while location_is_valid == False:
        location_is_valid = input('Please enter activity location or press q to exit: ')
        if location_is_valid == 'q': return 'q'
        if location_is_valid: activity_data['location'] = location_is_valid
    
    # return activity data dictionary
    return activity_data
            
if __name__ == '__main__':
    main()
