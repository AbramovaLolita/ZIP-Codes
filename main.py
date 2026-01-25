import zip_util as util
from commands import loc, codes, dist
if  util.read_zip_all() is None:
    print('Файл не обнаружен или назван некорректно')
else:
    zip_codes = util.read_zip_all()

commands = ('loc', 'zip', 'dist', 'end')
user_input = ''

while user_input != 'end':
    user_input = input("Command ('loc', 'zip', 'dist', 'end') => ")

    if user_input not in commands:
        print('Invalid command, ignoring')

    elif user_input == 'loc':
        while True:
            code = input("Enter a ZIP code to look up => ")
            if loc(zip_codes, code) is None:
                print(f'The ZIP code does not exist. Try again.')
                continue
            else:
                location, coordinates = loc(zip_codes, code)
                print(f"ZIP code {code} is in {', '.join(location)},{'\n'}coordinates {', '.join(coordinates)}")
            break

    elif user_input == 'zip':
        while True:
            city_name = input("Enter a city name to look up => ").capitalize()
            state_name = input("Enter a state name to look up => ").upper()
            if codes(zip_codes, city_name, state_name) is None:
                print(f'The city name or state name are incorrect. Try again.')
                continue
            else:
                indexes = codes(zip_codes, city_name, state_name)
                print(f"The following ZIP-codes found for {city_name}, {state_name}: {', '.join (indexes)}")
            break

    elif user_input == 'dist':
        while True:
            code_1 = input("Enter the first ZIP code => ")
            code_2 = input("Enter the second ZIP code => ")
            distance = dist(zip_codes, code_1, code_2)
            if result := dist(zip_codes, code_1, code_2) is None:
                print(f'The ZIP code is incorrect. Try again.')
                continue
            else:
                print(f"The distance between {code_1} and {code_2} is {distance:.2f} miles.")
            break

    elif user_input == 'end':
        print('Done!')
        continue
