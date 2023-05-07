from flask import Flask
from celery import Celery
import db as db

app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# Example of a Celery task
@celery.task
def add(a, b):
    return a + b

@app.route("/")
def hello():
    print(db.pull_data())
    return db.pull_data()

@app.route("/ebay.api")
def epbay():
    print(db.pull_data())
    return db.pull_data()

@app.route("/amazony.api")
def amazony():
    print(db.pull_data())
    return db.pull_data()

if __name__ == "__main__":
    app.run(debug=True)
