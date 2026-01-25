
def read_zip_all():
    '''
    @requires: CVS-файл со списком данных о почтовых индексах в формате:
    "zip_code","latitude","longitude","city","state","county"
    "04431",44.561174,-68.664735,"East Orland","ME","Hancock"
    @modifies: None
    @effects: None
    @raises: FileNotFoundError
    @returns: словарь индексов. Ключ - индекс(строка),
    значения: широта (значение дано в градусах, тип данных float),
    долгота (значение дано в градусах, тип данных float),
    город (строка), штат (строка) и графство (строка), например:
    '99821': [58.449413, -134.700348, 'Auke Bay', 'AK', 'Juneau'],
    '''
    i = 0
    header = []
    zips = {}
    skip_line = False
    # http://notebook.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv
    try:
        for line in open('zip_codes_states.csv').read().split("\n"):
            skip_line = False
            m = line.strip().replace('"', '').split(",")
            i += 1
            if i == 1:
                for val in m:
                    header.append(val)
            else:
                zip_data = {}
                for idx in range(0, len(m)):
                    if m[idx] == '':
                        skip_line = True
                        break
                if not skip_line:
                   zip_data = {m[0]:
                                [float(m[idx]) if header[idx] in("latitude", "longitude" )  else m[idx] for idx in range(1, len(m))]}
                   zips.update(zip_data)
        return zips
    except FileNotFoundError:
        return None

if __name__ == "__main__":
    zips = read_zip_all()

    assert len(zips) == 42049, \
        f'The number of ZIP codes read is {len(zips)} instead of 42049'
    print(zips['12180'])
    assert zips['12180'] == \
        [42.673701, -73.608792, 'Troy', 'NY', 'Rensselaer'], \
        'Properties of ZIP 12180 are incorrect'
    print(zips['99950'])
    assert zips['99950'] == \
        [55.542007, -131.432682, 'Ketchikan', 'AK', 'Ketchikan Gateway'], \
        'Properties of ZIP 99950 are incorrect'
    for elem in zips:
        assert elem[1] is not None and elem[1] != 0.0, \
            f'Latitude of ZIP {elem[0]} is {elem[1]} which is invalid'
        assert elem[2] is not None and elem[2] != 0.0, \
            f'Latitude of ZIP {elem[0]} is {elem[2]} which is invalid'
    print('All tests passed!')
