"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="1234567"
)

cur = conn.cursor()

with open('north_data/customers_data.csv') as f:
    next(f)
    cur.copy_expert('COPY customers FROM stdin WITH CSV', f)

with open('north_data/orders_data.csv') as f:
    next(f)
    cur.copy_expert('COPY orders FROM stdin WITH CSV', f)

with open('north_data/employees_data.csv') as f:
    next(f)
    cur.copy_expert('COPY employees FROM stdin WITH CSV', f)

conn.commit()

cur.close()
conn.close()
