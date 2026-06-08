"""
tələbələr cədvəlini yaradın və 5 tələbə üçün məlumat əlavə edin.
Bütün tələbələrin ad və yaşını ekrana çıxarın.
20 yaşdan böyük tələbələri seçin.
Bir tələbənin yaşını dəyişdirin.
Bir tələbəni silin.
Yeni sütun (address) əlavə edin və hər tələbəyə ünvan məlumatı daxil edin.
Tələbələrin yaşına görə ORDER BY əməliyyatını yerinə yetirin.
DISTINCT və COUNT funksiyalarından istifadə edərək unikal yaşları və neçə tələbənin müəyyən yaşda olduğunu tapın.
"""
import sqlite3

conn = sqlite3.connect('telebeler.db')
cursor = conn.cursor()

#1
cursor.execute('''CREATE TABLE IF NOT EXISTS telebeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
  	ad TEXT,
  	soyad TEXT,
  	ad_gunu DATE,
  	email TEXT
)''')
cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Narmin', 'Seyidbayli', '2004-06-22', 'narminm@gmail.com')")
cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Orxan', 'Ahmadli', '2005-10-20', 'orxanahm@gmail.com')")
cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Ahmad', 'Ahmadli', '2005-10-15', 'ahmadm@gmail.com')")
cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Huseyn', 'Ahmadov', '1999-02-02', 'huseyn@gmail.com')")
cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Zahid', 'Aziz', '2007-02-05', 'zahid@gmail.com')")

#2
cursor.execute("SELECT ad, (strftime('%Y', 'now') - strftime('%Y', ad_gunu)) AS yas FROM telebeler")
rows = cursor.fetchall()
for row in rows:
    print(f'Name: {row[0]}, Age: {row[1]}')

#3
cursor.execute("ALTER TABLE telebeler ADD COLUMN yas INTEGER")
cursor.execute('''
    UPDATE telebeler 
    SET yas = strftime('%Y', 'now') - strftime('%Y', ad_gunu)
''')
cursor.execute("SELECT ad, yas FROM telebeler WHERE yas > 20")
for row in cursor.fetchall():
    print(row)

#4
cursor.execute('''
    UPDATE telebeler 
    SET yas = 25 
    WHERE id = 1
''')
for row in cursor.fetchall():
    print(row)

#5
cursor.execute('''
    DELETE FROM telebeler 
    WHERE id = 5
''')
for row in cursor.fetchall():
    print(row)

#6
cursor.execute("ALTER TABLE telebeler ADD COLUMN address TEXT")
cursor.execute('''
    UPDATE telebeler 
    SET address = 'Baku, Natig Aliyev Str.' 
    WHERE id = 1
''')
cursor.execute('''
    UPDATE telebeler 
    SET address = 'Baku, Nizami Str.' 
    WHERE id = 2
''')
cursor.execute('''
    UPDATE telebeler 
    SET address = 'Ganja, Ataturk Ave.' 
    WHERE id = 3
''')
cursor.execute('''
    UPDATE telebeler 
    SET address = 'Nakhchivan, Aziz Aliyev Ave.' 
    WHERE id = 4
''')
cursor.execute('''
    UPDATE telebeler 
    SET address = 'Shusha, Karabakh Str.' 
    WHERE id = 5
''')

#7
cursor.execute('''
    SELECT * FROM telebeler ORDER BY yas DESC
''')
for row in cursor.fetchall():
    print(row)

#8
cursor.execute('''
    SELECT yas, COUNT(id) AS telebe_sayi
    FROM telebeler
    GROUP BY yas
    ORDER BY yas
''')


rows = cursor.fetchall()
print("Yas | Telebe Sayi")
print("-----------------")
for row in rows:
    print(f"{row[0]} yas -> {row[1]} telebe")

conn.commit()
conn.close()
