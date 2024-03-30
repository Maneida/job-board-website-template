#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, render_template, jsonify
import database

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    jobs = database.load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='Jovian',
                           year=datetime.now().year)


@app.route('/api/v1/jobs', strict_slashes=False)
def list_jobs():
    jobs = database.load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
