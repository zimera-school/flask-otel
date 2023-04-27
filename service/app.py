from flask import Flask

import psycopg
from psycopg.rows import dict_row

import os

conn = psycopg.connect(
        host=os.environ['DB_HOST'],
        dbname=os.environ['DB_DBNAME'],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
		row_factory=dict_row)

app = Flask(__name__)

@app.route('/')
def slash():
	return "flask-otel: instrumented Flask RESTful API using OpenTelemetry"

@app.route('/organization')
def slash_organization():
	cur = conn.cursor()
	cur.execute('select * from organization')
	return cur.fetchall()

@app.route('/organization/<id>')
def slash_organization_by_id(id):
	cur = conn.cursor()
	cur.execute("select * from organization where organization_id=%s;", (id,))
	return cur.fetchall()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
