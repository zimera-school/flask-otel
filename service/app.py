from flask import Flask

from opentelemetry import trace

import psycopg
from psycopg.rows import dict_row

import os

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Service name is required for most backends,
# and although it's not necessary for console export,
# it's good to set service name anyways.
resource = Resource(attributes={
    SERVICE_NAME: "hr_service"
})

jaeger_exporter = JaegerExporter(
    agent_host_name="localhost",
    agent_port=6831,
)

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

# Acquire a tracer
tracer = trace.get_tracer(__name__)

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
	with tracer.start_as_current_span("select_by_id") as sbi:
		cur = conn.cursor()
		cur.execute("select * from organization where organization_id=%s;", (id,))
		sbi.set_attribute("get_id: ", id)
		return cur.fetchall()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
