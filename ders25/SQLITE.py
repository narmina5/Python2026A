"""
CREATE TABLE IF NOT EXISTS telebeler (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	ad,
  	soyad,
  	ad_gunu,
  	email
);

SELECT * FROM telebeler;
SELECT ad, email FROM telebeler;

INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Orxan', 'Ahmadli', '20-10-2005', 'orxanahm@gmail.com');
INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Ahmad', 'Ahmadli', '15-10-2005', 'ahmadm@gmail.com');
INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Huseyn', 'Ahmadov', '02-02-1999', 'huseyn@gmail.com');
INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Zahid', 'Aziz', '20-02-2007', 'zahid@gmail.com');
INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Shamil', 'Sadigov', '02-10-2002', 'shamil@gmail.com');
INSERT INTO telebeler (ad, soyad, ad_gunu, email) VALUES ('Murad', 'Ahmadli', '20-10-2005', 'murad@gmail.com');

SELECT * from telebeler WHERE ad IN ('Huseyn', 'Shamil', 'Ahmad');
SELECT * from telebeler WHERE ad='Huseyn' or ad='Shamil' OR ad='Ahmad';

SELECT * from telebeler WHERE Not ad='Huseyn';
SELECT * from telebeler WHERE ad='Huseyn' limit 3;

UPDATE telebeler SET email='huseynahmadoff@gmail.com' WHERE email='huseyn@gmail.com';

SELECT * FROM telebeler WHERE soyad LIKE 'Ahm%';
SELECT * FROM telebeler WHERE soyad LIKE '%i%';
SELECT * FROM telebeler WHERE soyad LIKE '%li';

SELECT * FROM telebeler ORDER BY ad DESC;


SELECT * FROM telebeler WHERE ad='Huseyn' ORDER BY ad DESC LIMIT 3;

SELECT * FROM telebeler GROUP BY ad_gunu;
"""