#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='Jovian',
                           year=datetime.now().year)


@app.route('/api/v1/jobs', strict_slashes=False)
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route('/job/<id>')
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template("jobpage.html", job=job, company_name='Jovian')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
