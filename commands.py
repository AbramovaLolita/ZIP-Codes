import math
import zip_util as util
zip_codes = util.read_zip_all()
DEBUG = True

#радиус земли в милях
R = 3959

def degrees_to_dms(coordinates):
    '''
    @requires: coordinates - кортеж из двух координат
    @modifies: None
    @effects: функция loc()
    @raises: None
    @returns: lat_dms, long_dms - координаты в формате 'градусы-минуты-секунды'
    '''
    try:
        lat, long = coordinates

        sn = '"N' if lat >= 0 else '"S'
        degree_lat = abs(int(lat))
        minute_lat = (abs(lat) - abs(degree_lat)) * 60
        second_lat = (minute_lat - (int(minute_lat))) * 60

        we = '"E' if long >= 0 else '"W'
        degree_long = abs(int(long))
        minute_long = (abs(long) - abs(degree_long)) * 60
        second_long = (minute_long - (int(minute_long))) * 60
        apostrophe = "'"
        lat_dms = f"{degree_lat}\N{DEGREE SIGN}{int(minute_lat)}{apostrophe}{second_lat:.2f}{sn}"
        long_dms = f"{degree_long}\N{DEGREE SIGN}{int(minute_long)}{apostrophe}{second_long:.2f}{we}"
        return lat_dms, long_dms
    except KeyError or TypeError:
        return None

def loc(zips, code_1):
    '''
    @requires: словарь индексов в формате:
    '99789': [66.693255, -153.993988, 'Nuiqsut', 'AK', 'North Slope']
    @modifies: None
    @effects: None
    @raises: TypeError; KeyError, если индекс отсутствует в словаре
    @returns: кортеж location, coordinates из значения словаря, полученного по ключу code_1
    '''
    try:
        location = zips[code_1][2:]
        if not degrees_to_dms(zip_codes[code_1][:2]) is None:
            coordinates =  degrees_to_dms(zip_codes[code_1][:2])
            return location, coordinates
        else:
            return None
    except KeyError:
        return None
    except TypeError:
        return None

def codes(zips, city_name, state_name):
    '''
    @requires:
    словарь индексов в формате:
    '99789': [66.693255, -153.993988, 'Nuiqsut', 'AK', 'North Slope'],
    city_name - название города в виде строки, state_name - название штата в виде строки
    @modifies: None
    @effects: None
    @raises: TypeError
    @returns: codes - список индексов, которые являются ключами словаря со значениями city_name и state_name
    '''
    try:
        indexes = [key for key, value in zips.items() if city_name in value and state_name in value]
        if len(indexes) == 0:
           return None
        else:
            return indexes
    except TypeError:
        return None


def dist(zips, code_1, code_2):
    '''
    @requires: словарь индексов в формате:
    '99789': [66.693255, -153.993988, 'Nuiqsut', 'AK', 'North Slope'],
    два индекса (code_1, code_2) для вычисления расстояния формате строк
    @modifies: None
    @effects: None
    @raises: TypeError, KeyError
    @returns: d - расстояние между введенными индексами, рассчитанное по формуле Гаверсина
    '''
    try:
        lat_1 = math.radians(zips[code_1][0])
        long_1 = math.radians(zips[code_1][1])
        lat_2 = math.radians(zips[code_2][0])
        long_2 = math.radians(zips[code_2][1])

        d \
            = 2 * R * math.asin(math.sqrt(math.pow(math.sin((lat_2 - lat_1) / 2), 2) + math.cos(lat_1) * math.cos(lat_2) * math.pow(math.sin((long_2 - long_1) / 2), 2)))
        return d
    except KeyError or TypeError:
        return None


if DEBUG:
    # test degrees_to_dms()
    expected = \
        ('44°47\'30.08"N', '68°34\'39.82"W')
    actual = degrees_to_dms((44.79169,-68.577728))
    if actual != expected:
        print('Test degrees_to_dms failed!')

    # test codes()
    expected = \
          ['61920']
    actual = codes(zip_codes, 'charleston'.capitalize(), 'il'.upper())
    if actual != expected:
        print('Test code failed!')

    # test loc()
    code = loc(zip_codes, '12019')
    expected = \
        (['Ballston Lake', 'NY', 'Saratoga'], ('42°56\'3.90"N', '73°50\'56.30"W'))
    actual = loc(zip_codes, '12019')
    if actual != expected:
        print('Test loc failed!')

    # test dist()
    expected = \
    2.2200099363164045
    actual = dist(zip_codes, '04412', '04444')
    if actual != expected:
        print('Test dist failed!')
else:
    zip_codes = util.read_zip_all()