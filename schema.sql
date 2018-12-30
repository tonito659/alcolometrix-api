--
-- Fichier généré par SQLiteStudio v3.2.1 sur mer. dec. 05 15:28:19 2018
--
-- Encodage texte utilisé : System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

DROP TABLE IF EXISTS alcolometrix_api;

-- Table : Base_de_donnée
CREATE TABLE IF NOT EXISTS alcolometrix_api (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  date INTEGER NOT NULL,
  barcode INTEGER NOT NULL,
  price REAL NOT NULL,
  postcode TEXT NOT NULL,
  localization TEXT NOT NULL);

INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (2, '1544628032', 7312040017355, 19, 92100,  'Boulogne-Billancourd');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (3, '1544628032', 3163937010003, 25, 92100,'Boulogne-Billancourd');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (4, '1544628032', 5099873006504, 27.2, 92100,'Boulogne-Billancourd');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (1, '1544628032', 5410769100081, 2.5, 92100,'Boulogne-Billancourd');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (5, '1544628032', 3099873045864, 28, 92100,'Boulogne-Billancourd');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (6, '1544628032', 7312040017355, 19, 92000,'Nanterre');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (7, '1544628033', 3163937010003, 20, 92200,'Suresnes');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (8, '1544628032', 3163937010003, 18.6, 92140,'Clamart');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (9, '1544628032', 3163937010003, 40.3, 92000,'Nanterre');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (10, '1544628032', 3163937010003, 27.4, 92000,'Nanterre');
INSERT INTO alcolometrix_api (id, date, barcode, price, postcode, localization) VALUES (11, '1544628032', 3163937010003, 30.4, 92000,'Nanterre');


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;