import sqlite3
import pandas as pd

conn = sqlite3.connect('maimai_info.db')
print("Opened database successfully")

c = conn.cursor()
c.execute('''
    CREATE TABLE MAIMAI_MUSIC_INFO(
        ID INT,
        CATEGORY TEXT,
        MUSIC_NAME TEXT,
        DIFFICULTY TEXT,
        STARS TEXT,
        SD_OR_DX TEXT,
        PRIMARY KEY(ID)
    );
''')
print("Table created successfully")

data_info = pd.read_csv('./csv_file/maimai_full_list_edited.csv')

for i, datas in data_info.iterrows():
    category = datas['Category']
    music_name = datas['Music_name']
    difficulty = datas['Difficulty']
    stars = datas['Stars']
    stars_in_detail = datas['Stars_in_detail']
    sd_or_dx = datas['SD_or_DX']

    print(datas)
    c.execute(
        "INSERT INTO MAIMAI_MUSIC_INFO (ID, CATEGORY, MUSIC_NAME, DIFFICULTY, STARS, SD_OR_DX) \
         VALUES ('%d', '%s', '%s', '%s', '%s', '%s')" % (i, category, music_name, difficulty, stars, sd_or_dx)
    )

conn.commit()
conn.close()
