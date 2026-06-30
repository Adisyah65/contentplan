import sqlite3
import re

# koneksi SQLite
conn = sqlite3.connect("contentplan.db")
cursor = conn.cursor()

# baca file dump MySQL
with open("contentplan_dump.sql", "r", encoding="utf-8") as f:
    sql = f.read()

# ===== CLEAN MYSQL -> SQLITE =====
sql = re.sub(r"CREATE DATABASE.*?;", "", sql)
sql = re.sub(r"USE .*?;", "", sql)
sql = re.sub(r"ENGINE=.*?;", ";", sql)
sql = re.sub(r"AUTO_INCREMENT", "", sql)
sql = re.sub(r"DEFAULT CHARSET=.*?;", ";", sql)
sql = re.sub(r"COLLATE.*? ", " ", sql)
sql = re.sub(r"unsigned", "", sql, flags=re.IGNORECASE)

# jalankan ke sqlite
cursor.executescript(sql)
conn.commit()
conn.close()

print("IMPORT BERHASIL 🚀")