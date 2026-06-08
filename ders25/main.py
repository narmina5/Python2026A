# https://sqliteonline.com/
"""
CREATE TABLE <table_name> (col1 INTEGER, col2 TEXT, col3 TEXT);
INSERT INTO <table_name> (col1, col2, col3) VALUES (val1, val2, val3);
SELECT col1, col2, col3 FROM <table_name>;
UPDATE <table_name> SET col1 = val1, col2 = val2, col3 = val3 WHERE ...;
DELETE FROM <table_name> WHERE ...;
DROP TABLE <table_name>;
ALTER TABLE <table_name> ADD COLUMN <column_name> INTEGER;
ALTER TABLE <table_name> DROP COLUMN <column_name>;
ALTER TABLE <table_name> ALTER COLUMN <column_name> TYPE INTEGER;
ALTER TABLE <table_name> RENAME COLUMN <old_column_name> TO <new_column_name>;
 ----- ALTER TABLE <table_name> ALTER COLUMN <column_name> SET DEFAULT <value>;

CREATE INDEX
DROP INDEX
COMMENT ON

=========================================================
DATATYPES

Numbers (whole):
    SMALLINT    -  2bytes   - -32K:32K
    INTEGER     -  4bytes   - -2B:2B
    BIGINT      -  8bytes   - very large integer values

Fractional:
    REAL                - 6 digits after comma
    DOUBLE PRECISION    - 15 digits after comma
    FLOAT               - dynamic

Date:
    DATE    - Date (YYYY-MM-DD)
    TIME    - Time without timezone
    TIME WITH TIME ZONE - Time with timezone
    TIMESTAMP (seconds since 01.01.1970) - Date + time without timezone
    TIMESTAMP WITH TIME ZONE - Date + time with timezone
    INTERVAL - A span of time (e.g. '2 days 3 hours')

Bool:
    BOOLEAN - Holds TRUE, FALSE, NULL

Geometric Types:
    POINT   | (x, y) coordinates
    LINE    | Infinite line
    LSEG    | Line segment
    BOX     | Rectangular box
    CIRCLE  | Circle
    POLYGON | Polygon

Text:
    TEXT - String

=========================================================

=====================================================================
Exercise 1...

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name TEXT,
  age INTEGER DEFAULT 0,
  height FLOAT(2),
  have_siblings BOOLEAN,
  birthdate TIMESTAMP
);

DROP TABLE students;

SELECT name, height FROM students;

INSERT INTO students (name, age, height, have_siblings, birthdate) VALUES ('Random1', 12, 158.40, TRUE, TO_TIMESTAMP(941019325));
INSERT INTO students (name, age, height, have_siblings, birthdate) VALUES ('Random2', 24, 158.40, TRUE, TO_TIMESTAMP(941019325));
INSERT INTO students (name, age, height, have_siblings, birthdate) VALUES ('Random3', 45, 188.40, TRUE, TO_TIMESTAMP(911019325));
INSERT INTO students (name, age, height, have_siblings, birthdate) VALUES ('Random6', 12, 138.40, TRUE, '1999-07-17 06:15:25');
INSERT INTO students (name, have_siblings) VALUES ('Random3', TRUE);

DELETE FROM students WHERE name LIKE 'random%';

SELECT * FROM students;

UPDATE students SET age=30 WHERE name='Random2';

ALTER TABLE students ADD COLUMN address TEXT;
ALTER TABLE students DROP COLUMN address;

=====================================================================
WHERE
IN -- SELECT * FROM students WHERE name IN ('Random1', 'Random2', 'Random3');
IN -- SELECT * FROM students WHERE name = 'Random1';
IN -- SELECT * FROM students WHERE name LIKE 'Random%';

ORDER BY -- SELECT * FROM students ORDER BY age;
ASC -- SELECT * FROM students ORDER BY age ASC;
DESC -- SELECT * FROM students ORDER BY age DESC;
COUNT -- SELECT COUNT(*) FROM students WHERE age>15;
GROUP BY -- SELECT * FROM students GROUP BY age;
LIMIT -- SELECT * FROM students LIMIT 3;
DISTINCT -- SELECT DISTINCT ON (height) name, age, height FROM students; / SELECT DISTINCT ON (height) * FROM students;
LIKE -- SELECT * FROM students WHERE name LIKE 'Random%';
ILIKE -- SELECT * FROM students WHERE name ILIKE 'Random%';
    Symbol  | Meaning                   | Example
        %   | zero or more characters   | 'A%' matches 'Alice', 'Alex', 'America'
        _   | exactly one character     | 'A_' matches 'Al', 'An', 'At'
ON
DEFAULT -- ...age INTEGER DEFAULT 0,...
JOIN
LEFT JOIN
HAVING

COPY CSV HEADER

PRIMARY KEY
FOREIGN KEY
"""

"""
CREATE TABLE IF NOT EXISTS posts (
  id TEXT PRIMARY KEY,
  header TEXT,
  body TEXT NOT NULL
);

INSERT INTO posts (id, header, body) VALUES (15, 'aa', 'bodyy');
INSERT INTO posts (id, header, body) VALUES (16, 'as', 'd');
INSERT INTO posts (id, header, body) VALUES (17, 'SAD', 'boddyy');
INSERT INTO posts (id, header, body) VALUES (18, 'AS', 'bosddyy');
INSERT INTO posts (id, header, body) VALUES (19, 'ASD', 'as');
INSERT INTO posts (header, body) VALUES ('D', 'boddyy');

SELECT * FROM posts;

UPDATE posts SET body = 'asdsd' WHERE header = 'AS';

DELETE FROM posts WHERE header = 'AS';

SELECT DISTINCT header FROM posts;

SELECT * FROM posts ORDER BY header DESC;

SELECT header, COUNT(*) AS post_count FROM posts GROUP BY header;
"""





import sqlite3

conn = sqlite3.connect('telebeler.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS telebeler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
  	ad,
  	soyad,
  	ad_gunu DATE,
  	email
)
''')
#cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Orxan', 'Ahmadli', '2005-10-20', 'orxanahm@gmail.com')")
#cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Ahmad', 'Ahmadli', '2005-10-15', 'ahmadm@gmail.com')")
#cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Huseyn', 'Ahmadov', '1999-02-02', 'huseyn@gmail.com')")
#cursor.execute("INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Zahid', 'Aziz', '2007-02-05', 'zahid@gmail.com')")


cursor.execute('SELECT * FROM telebeler')
print(cursor.fetchall())


conn.commit()

conn.close()




import sqlite3

# Qoşul
conn = sqlite3.connect('telebeler.db')
cursor = conn.cursor()

# Cədvəl yarat
cursor.execute('''
CREATE TABLE IF NOT EXISTS telebeler (
    id INTEGER PRIMARY KEY,
    ad TEXT,
    yas INTEGER
)
''')

# Məlumat əlavə et
cursor.execute('INSERT INTO telebeler (ad, yas) VALUES (?, ?)', ('Anar', 22))

# Məlumat oxu
cursor.execute('SELECT * FROM telebeler')
for satir in cursor.fetchall():
    print(satir)

# Bağla
conn.commit()
conn.close()
