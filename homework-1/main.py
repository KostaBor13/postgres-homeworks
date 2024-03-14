"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "1234"
}

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO customers (customer_id, company_name, contact_name)"
                            "VALUES (%s, %s, %s)", tuple(row))
        # получаем результат для проверки
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        for row in rows:
            print(row)
conn.close()

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)"
                            "VALUES (%s, %s, %s, %s, %s, %s)", tuple(row))

        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()
        for row in rows:
            print(row)
conn.close()

with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        with open('north_data/orders_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)"
                            "VALUES (%s, %s, %s, %s, %s)", tuple(row))

        cur.execute("SELECT * FROM orders")
        rows = cur.fetchall()
        for row in rows:
            print(row)
conn.close()