import zip_util as util
from commands import loc, code, dist, end
zip_codes = util.read_zip_all()

commands = ('loc', 'zip', 'dist', 'end')

user_input = input("Command ('loc', 'zip', 'dist', 'end') => ")


if user_input == 'loc':
    code = input("Enter a ZIP code to look up => ")
    location, coordinates = loc(zip_codes, code)
    print(f'ZIP code {code} is in {', '.join(location)},{'\n'}coordinates {','.join(coordinates)}')
if user_input == 'zip':
    city_name = input("Enter a city name to look up => ").capitalize()
    state_name = input("Enter a city name to look up => ").upper()
    code = code(zip_codes, city_name, state_name)
    print(f'The following ZIP-codes found for {city_name}, {state_name}: {', '.join (code)}')
if user_input == 'dist':
    code_1 = input("Enter the first ZIP code => ")
    code_2 = input("Enter the first ZIP code => ")
    distance = dist(zip_codes,code_1, code_2)
    print(f'The distance between {code_1} and {code_2} is {distance:.2f} miles.')