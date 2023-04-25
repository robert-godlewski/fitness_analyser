import sqlite3


conn = sqlite3.connect('sizesdata.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Size_Data (date TEXT, height FLOAT, weight FLOAT, forearms FLOAT, upperarms FLOAT, neck FLOAT, shoulders FLOAT, chest FLOAT, waist FLOAT, hip FLOAT, thighs FLOAT, calf FLOAT, notes TEXT, is_metric INTEGER)''')

fh = open('./csv_data/MyMeasurementsRelaxedOriginal.csv')
for line in fh:
    #print(line)
    if line.startswith('Date'): continue
    info = line.split(',')
    #print(info)
    data = {
        'date': None,
        # Need to fix this for the future
        'height': 68.0,
        'weight': None,
        'forearms': None,
        'upperarms': None,
        'neck': None,
        'shoulders': None,
        'chest': None,
        'waist': None,
        'hip': None,
        'thighs': None,
        'calf': None,
        'notes': None,
        # 0 for false and 1 for true in sqlite
        'is_metric': 0
    }

    #print(f'Date = {info[0]}')
    date_arr = info[0].split('/')
    data['date'] = f'{date_arr[2]}-{date_arr[0]}-{date_arr[1]}'
    #print('Height = 68 inches')
    #print(f'Weight = {info[1]} pounds')
    if info[1] != '':
        data['weight'] = float(info[1])
    else:
        data['weight'] = -1
    #print(f'Forearm Circumference around the thickest part = {info[2]} inches')
    data['forearms'] = float(info[2])
    #print(f'Upper Arms Circumference around the thickest part = {info[3]} inches')
    data['upperarms'] = float(info[3])
    #print(f'Neck Circumference around the adams apple = {info[4]} inches')
    data['neck'] = float(info[4])
    #print(f'Shoulders Circumference with shoulders pinched = {info[5]} inches')
    data['shoulders'] = float(info[5])
    #print(f'Chest Circumference around the nipples = {info[6]} inches')
    data['chest'] = float(info[6])
    #print(f'Waist Circumference around the belly button = {info[7]} inches')
    data['waist'] = float(info[7])
    #print(f'Hip Circumference around the thickest part = {info[8]} inches')
    data['hip'] = float(info[8])
    #print(f'Thighs Circumference 2 inches away from butt = {info[9]} inches')
    data['thighs'] = float(info[9])
    #print(f'Calfs Circumference around the thickest part = {info[10]} inches')
    data['calf'] = float(info[10])
    #print(f'Notes = {info[11]}')
    data['notes'] = info[11]

    print(data)

    # This below is not working for some reason
    try:
        cur.execute("SELECT * FROM Size_Data WHERE date = ?", (memoryview(data['date'].encode()), ))
    except:
        pass

    cur.execute('''INSERT INTO Size_Data (date, height, weight, forearms, upperarms, neck, shoulders, chest, waist, hip, thighs, calf, notes, is_metric) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        memoryview(data['date'].encode()),
        memoryview(data['height']),
        memoryview(data['weight'].encode()),
        memoryview(data['forearms'].encode()),
        memoryview(data['upperarms'].encode()),
        memoryview(data['neck'].encode()),
        memoryview(data['shoulders'].encode()),
        memoryview(data['chest'].encode()),
        memoryview(data['waist'].encode()),
        memoryview(data['hip'].encode()),
        memoryview(data['thighs'].encode()),
        memoryview(data['calf'].encode()),
        memoryview(data['notes'].encode()),
        memoryview(data['is_metric'].encode()),
    ))
    conn.commit()
    print('Entered in new data.')

print('Finish Importing the data')
print('********************************')
