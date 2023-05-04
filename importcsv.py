import sqlite3


# Gets the data from csv file and save it to a db.
def importCSV(filename: str, is_metric: bool) -> None:
    print(f"Importing {filename}")
    conn = sqlite3.connect('sizesdata.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Size_Data (date TEXT, height TEXT, weight TEXT, forearms TEXT, upperarms TEXT, neck TEXT, shoulders TEXT, chest TEXT, waist TEXT, hip TEXT, thighs TEXT, calf TEXT, notes TEXT, is_metric TEXT)''')
    fh = open(f'./csv_data/{filename}')
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
    print('Finish Importing the data')
    print('********************************')
