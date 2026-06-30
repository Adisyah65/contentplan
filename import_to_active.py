import sqlite3
import re
import os

db_path = r'C:\adisyah\semester 6\contentplan\instance\contentplan.db'
sql_dump_path = r'c:\Users\USER\Downloads\semester 6\contentplan\contentplan\contentplan_dump.sql'

if not os.path.exists(db_path):
    print(f"Error: Target database not found at {db_path}")
    exit(1)

if not os.path.exists(sql_dump_path):
    print(f"Error: SQL dump not found at {sql_dump_path}")
    exit(1)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Nonaktifkan foreign key checks untuk proses import data
cursor.execute("PRAGMA foreign_keys = OFF;")

# Bersihkan tabel lama agar tidak terjadi duplikat key error
tables = ['analytics', 'schedule', 'content', 'user']
for table in tables:
    cursor.execute(f"DELETE FROM `{table}`;")
    print(f"Mengosongkan tabel: {table}")

# Membaca isi file SQL dump
with open(sql_dump_path, 'r', encoding='utf-8') as f:
    sql_content = f.read()

# Ekstrak semua query INSERT INTO menggunakan regex
insert_queries = re.findall(r"(INSERT INTO `\w+`[\s\S]*?;)", sql_content)

insert_count = 0
for query in insert_queries:
    try:
        cursor.execute(query)
        insert_count += 1
    except Exception as e:
        print(f"Gagal menjalankan query:\n{query[:150]}...\nError: {e}")

conn.commit()
cursor.execute("PRAGMA foreign_keys = ON;")
conn.close()

print(f"\n[OK] Migrasi selesai! Berhasil memasukkan {insert_count} query data ke SQLite aktif.")
