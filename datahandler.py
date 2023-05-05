from converters import *
import sqlite3


# Gets the data from csv file and save it to a db.
def importCSV(filename: str, is_metric: bool) -> None:
    conn = sqlite3.connect('sizesdata.sqlite')
    cur = conn.cursor()
    print(f"Importing {filename}")
    cur.execute('''CREATE TABLE IF NOT EXISTS Size_Data (date TEXT PRIMARY KEY, height TEXT, weight TEXT, forearms TEXT, upperarms TEXT, neck TEXT, shoulders TEXT, chest TEXT, waist TEXT, hip TEXT, thighs TEXT, calf TEXT, notes TEXT, is_metric TEXT)''')
    #fh = open(f'./csv_data/{filename}')
    fh = open(f'./csv_data/MyMeasurements{filename}')
    for line in fh:
        #print(line)
        if line.startswith('Date'): continue
        info = line.split(',')
        #print(info)
        data = {
            'date': None,
            # Need to fix this for the future
            'height': info[1],
            'weight': info[2],
            'forearms': info[3],
            'upperarms': info[4],
            'neck': info[5],
            'shoulders': info[6],
            'chest': info[7],
            'waist': info[8],
            'hip': info[9],
            'thighs': info[10],
            'calf': info[11],
            'notes': info[12],
            # 0 for false and 1 for true in sqlite
            'is_metric': is_metric
        }
        # Need to fix the date so that it's formatted correctly
        #print(f'Date = {info[0]}')
        date_arr = info[0].split('/')
        date = f'{date_arr[2]}-{date_arr[0]}-{date_arr[1]}'
        data['date'] = date
        #print(f"Date = {data['date']} ({type(data['date'])})")
        #print(data)
        # This below is not working for some reason
        try:
            cur.execute("SELECT * FROM Size_Data WHERE date = ?", (memoryview(date.encode()), ))
            print(f'There is already an entry with {date} in the db.')
            continue
        except:
            print(f'Entering in {data}')
            pass
        cur.execute('''INSERT INTO Size_Data (date, height, weight, forearms, upperarms, neck, shoulders, chest, waist, hip, thighs, calf, notes, is_metric) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
            memoryview(data['date'].encode()),
            memoryview(data['height'].encode()),
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
        print('Entered in new data. All are saved as string values.')
    fh.close()
    conn.close()
    print('Finish Importing the data')
    print('********************************')


# Grabs the data from the db to be graphed
def getAll() -> list:
    data = []
    conn = sqlite3.connect('sizesdata.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Size_Data''')
    raw_data = cur.fetchall()
    #print(raw_data)
    for raw_info in raw_data:
        info = {
            'date': binaryToString(raw_info[0]),
            'height': binaryToFloat(raw_info[1]),
            'weight': binaryToFloat(raw_info[2]),
            'forearms': binaryToFloat(raw_info[3]),
            'upperarms': binaryToFloat(raw_info[4]),
            'neck': binaryToFloat(raw_info[5]),
            'shoulders': binaryToFloat(raw_info[6]),
            'chest': binaryToFloat(raw_info[7]),
            'waist': binaryToFloat(raw_info[8]),
            'hip': binaryToFloat(raw_info[9]),
            'thighs': binaryToFloat(raw_info[10]),
            'calf': binaryToFloat(raw_info[11]),
            'notes': binaryToString(raw_info[12]),
            # Will need this for later
            #'is_metric': 'false'
        }
        print(info)
        data.append(info)
    conn.close()
    return data
