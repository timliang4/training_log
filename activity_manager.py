import datetime
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
                act = Activity(date_time_location)
            # User wants to access an exisiting activity
            elif choice == 2: 
                print('hi')
            # User wants to exit
            else:
                print('Goodbye')
                want_to_continue = False

def get_date_time_location():
    activity_data = {}
    # get date
    date_is_valid = False
    while date_is_valid == False:
        date_is_valid = validate_date(input('Please enter activity date (mm/dd/yyyy) or press q to exit: '))
        if date_is_valid == 'q': return 'q'
    # get time
    datetime_is_valid = False
    while datetime_is_valid == False:
        datetime_is_valid = validate_time(input('Please enter activity time (hh:mm) or press q to exit: '), date_is_valid)
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

def validate_date(input_date):
    # If date is invalid then return False, if user enters 'q' then return 'q', if date is valid then return the date object
    if input_date == 'q':
        return 'q'
    split_date = input_date.split('/')
    # Check if the user entered two back slashes
    if len(split_date) != 3:
        return False
    # Check if the user entered numbers
    try: split_int_date = [int(element) for element in split_date]
    except ValueError: return False
    else: 
        # Check if the user entered a date that isn't in the future
        activity_date = datetime.datetime(split_int_date[2], split_int_date[0], split_int_date[1], 0, 0, 0)
        if activity_date > datetime.datetime.now():
            return False
        # Return the valid date
        return activity_date

def validate_time(input_time, activity_date):
    # If timd is invalid then return False, if user enters 'q' then return 'q', if time is valid then return the time object
    if input_time == 'q':
        return 'q'
    split_time = input_time.split(':')
    # Check if the user entered one colon
    if len(split_time) != 2:
        return False
    # Check if the user entered numbers
    try: split_int_time = [int(element) for element in split_time]
    except ValueError: return False
    else:
        # Add the time to the existing activity_date datetime object
        activity_datetime = activity_date.replace(hour=split_int_time[0])
        activity_datetime = activity_datetime.replace(minute=split_int_time[1])
        if activity_datetime > datetime.datetime.now():
            return False
        # return the valid datetime
        return activity_datetime
            
if __name__ == '__main__':
    main()

