import sqlite3
import pandas as pd

conn = sqlite3.connect('test.db')
print("Opened database successfully")

c = conn.cursor()
c.execute('''
    CREATE TABLE MAIMAI_MUSIC_INFO(
        ID INT,
        CATEGORY TEXT,
        MUSIC_NAME TEXT,
        DIFFICULTY TEXT,
        STARS TEXT,
        STARS_IN_DETAIL TEXT,
        SD_OR_DX TEXT,
        PRIMARY KEY(ID)
    );
''')
print("Table created successfully")

data_info = pd.read_csv('./csv_file/maimai_full_list_edited.csv')

for i, datas in data_info.iterrows():
    category = data_info['Category']
    music_name = data_info['Music_name']
    difficulty = data_info['Difficulty']
    stars = data_info['Stars']
    stars_in_detail = data_info['Stars_in_detail']
    sd_or_dx = data_info['SD_or_DX']

    print(datas)
    c.execute(
        "INSERT INTO MAIMAI_MUSIC_INFO (ID, CATEGORY, MUSIC_NAME, DIFFICULTY, STARS, STARS_IN_DETAIL, SD_OR_DX) \
         VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s')" % (i, category, music_name, difficulty, stars, stars_in_detail, sd_or_dx)
    )

conn.commit()
conn.close()
