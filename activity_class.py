from datetime import datetime

class Activity:
    def __init__(self, activity_data, existing_activity):
        self.data = activity_data
        self.want_to_continue = True
        # If not an existing activity, add an exercises key-value pair in the data dictionary
        if not existing_activity:
            self.data['exercises'] = {}
        # If existing activity, turn date and time string into datetime object
        if existing_activity:
            date_string = self.data['date and time'] 
            self.data['date and time'] = datetime.strptime(date_string, '%m/%d/%Y %H:%M')
        # Prompt user with options
        while self.want_to_continue:
            print(50*'-')
            print('ACTIVITY OPTIONS')
            self.display_data()
            try:
                choice = int(input('''Please select from the following:
                            1 - set date and time
                            2 - set location
                            3 - set exercises
                            4 - write activity
                            5 - exit activity options\n'''))
            except ValueError: print("Please enter 1, 2, 3, 4, or 5")
            else:
                if choice == 1:
                    date_is_valid = False
                    while date_is_valid == False:
                        date_is_valid = Activity.validate_date(input('Please enter activity date (mm/dd/yyyy) or press q to exit: '))
                        if date_is_valid == 'q': return 'q'
                    # get time
                    datetime_is_valid = False
                    while datetime_is_valid == False:
                        datetime_is_valid = Activity.validate_time(input('Please enter activity time (hh:mm) or press q to exit: '), date_is_valid)
                        if datetime_is_valid == 'q': return 'q'
                        if datetime_is_valid: self.data['date and time'] = datetime_is_valid
                elif choice == 2:
                    location_is_valid = False
                    while location_is_valid == False:
                        location_is_valid = input('Please enter activity location or press q to exit: ')
                        if location_is_valid == 'q': return 'q'
                        if location_is_valid: self.data['location'] = location_is_valid
                elif choice == 3:
                    self.set_exercises()
                elif choice == 4:
                    self.write_data()
                elif choice == 5:
                    self.want_to_continue = False
                else:
                    print('Please enter 1, 2, 3, 4, or 5')



    def display_data(self):
        for pair in self.data.items():
            if pair[0] == 'exercises':
                if len(pair[1]) == 0:
                    print(f'{pair[0]} - none entered')
                    continue
                print(pair[0])
                for exercise in self.data[pair[0]].items():
                    print(f'    {exercise[0]}')
                    for measurement in self.data[pair[0]][exercise[0]].items():
                        print(f'        {measurement[0]}: {measurement[1]}')
                continue
            print(f'{pair[0]} - {pair[1]}')

    def set_date(self):
        # set date
        pass

    def set_time(self):
        # set time
        pass

    def set_location(self):
        # set location
        pass

    def set_exercises(self):
        choice_is_valid = False
        while choice_is_valid == False:
            print(50*'-')
            choice = input('Cardio or reps? (c, r, or q to return to activity options): ')
            if choice == 'c':
                self.add_cardio()
                choice_is_valid = True
            elif choice == 'r':
                self.add_rep_exercise()
                choice_is_valid = True
            elif choice == 'q':
                return
            else:
                print('Please enter c, r, or q')

    def add_cardio(self):
        # prompt for specific cardio workout, time, and distance
        cardio_exercises = {'run': {'miles': 0, 'minutes': 0}, 
                            'bike': {'miles': 0, 'minutes': 0}, 
                            'walk': {'miles': 0, 'minutes': 0},
                            'row': {'meters': 0, 'minutes': 0}}
        cardio_exercises_names = tuple(cardio_exercises.keys())
        choice_is_valid = False
        while choice_is_valid == False:
            print(50*'-')
            for index, exercise in enumerate(cardio_exercises_names):
                print(f'{index + 1} - {exercise}')
            choice = input('Please select from the cardio exercises above or press q to return to activity options: ')
            if choice == 'q':
                return
            try: choice = int(choice) - 1
            except ValueError: print('Please enter q or a number 1-4: ')
            else: 
                if choice not in (0, 1, 2, 3):
                    print("Please enter q or a number 1-4")
                    continue
                for measurement in cardio_exercises[cardio_exercises_names[choice]]:
                    valid_input = False
                    q_entered = False
                    while valid_input == False:
                        print(50*'-')
                        num = input(f'Enter {measurement} or press q to return to activity options: ')
                        if num == 'q':
                            q_entered = True
                            break
                        if Activity.is_float(num):
                            valid_input = True
                            cardio_exercises[cardio_exercises_names[choice]][measurement] = num
                    if q_entered:
                        break
                else: 
                    self.data['exercises'][cardio_exercises_names[choice]] = cardio_exercises[cardio_exercises_names[choice]]
                choice_is_valid = True
             
    def add_rep_exercise(self):
        rep_exercises = {'pushups': {'reps': 0},
                         'squats': {'reps': 0},
                         'curls': {'reps (per arm)': 0},
                         'planks': {'time (minutes)': 0},
                         'dead hangs': {'time (minutes)': 0},
                         'rows': {'reps': 0}}
        choice_is_valid = False
        rep_exercises_names = tuple(rep_exercises.keys())
        while choice_is_valid == False:
            print(50*'-')
            for index, name in enumerate(rep_exercises_names):
                print(f'{index + 1} - {name}')
            choice = input('Please select from the cardio exercises above or press q to return to activity options: ')
            if choice == 'q':
                return
            try: choice = int(choice) - 1
            except ValueError: print('Please enter q or 1-6')
            else:
                if choice not in [0, 1, 2, 3, 4, 5]:
                    print('Please enter q or 1-6')
                    continue
                for measurement in rep_exercises[rep_exercises_names[choice]]:
                    measurement_is_valid = False
                    q_entered = False
                    while measurement_is_valid == False:
                        print(50*'-')
                        input_measurement = input(f'Enter {measurement} or press q to return to activity options: ')
                        if input_measurement == 'q':
                            q_entered = True
                            break
                        if Activity.is_float(input_measurement):
                            rep_exercises[rep_exercises_names[choice]][measurement] = input_measurement
                            measurement_is_valid = True
                    if q_entered == True:
                        break
                else:
                    self.data['exercises'][rep_exercises_names[choice]] = rep_exercises[rep_exercises_names[choice]]
                choice_is_valid = True

    def write_data(self):
        activity_date = self.data['date and time']
        # write dictionary to a txt file
        file_name = 'activity_log/' + activity_date.strftime('%m_%d_%Y__%H_%M')
        # change date and time object back to a string
        self.data['date and time'] = activity_date.strftime('%m/%d/%Y %H:%M')
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(str(self.data))
        print('done')
    
    @staticmethod
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
            activity_date = datetime(split_int_date[2], split_int_date[0], split_int_date[1], 0, 0, 0)
            if activity_date > datetime.now():
                return False
            # Return the valid date
            return activity_date
    @staticmethod
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
            if activity_datetime > datetime.now():
                return False
            # return the valid datetime
            return activity_datetime

    @staticmethod
    def is_float(num):
        return num.replace('.', '').isnumeric()
