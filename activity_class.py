import datetime

class Activity:
    def __init__(self, activity_data):
        self.data = activity_data
        self.want_to_continue = True
        # Add an exercises key-value pair in the data dictionary
        self.data['exercises'] = {}
        # Prompt user with options
        while self.want_to_continue:
            print(50*'-')
            print('ACTIVITY OPTIONS')
            self.display_data()
            try:
                choice = int(input('''Please select from the following:
                            1 - set date
                            2 - set time
                            3 - set location
                            4 - set exercises
                            5 - write activity
                            6 - exit activity options\n'''))
            except ValueError: print("Please enter 1, 2, 3, 4, 5, or 6")
            else:
                if choice == 1:
                    pass
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    self.set_exercises()
                elif choice == 5:
                    self.write_data()
                elif choice == 6:
                    self.want_to_continue = False
                else:
                    print('Please enter 1, 2, 3, 4, 5, or 6')



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
        # write dictionary to a txt file
        file_name = 'activity_log/' + self.data['date and time'].strftime('%m_%d_%Y__%H_%M')
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(str(self.data))
        print('done')

    def exit(self):
        # exit 
        pass
    
    @staticmethod
    def is_float(num):
        return num.replace('.', '').isnumeric()