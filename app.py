#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

year = datetime.now().year


@app.route('/', strict_slashes=False)
def hello_world():
    jobs = load_jobs_from_db()
    return render_template("home.html", jobs=jobs, company_name='Jovian',
                           year=year)


@app.route('/api/v1/jobs', strict_slashes=False)
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route('/job/<id>', strict_slashes=False, methods=['POST', 'GET'])
def show_job(id):
    if request.method == 'POST':
        data = request.form
        data = dict(data)
        if add_application_to_db(id, data):
            return render_template("application_submitted.html",
                                   company_name='Jovian', application=data,
                                   year=year)
        else:
            return "Failed to submit application"

    job = load_job_from_db(id)
    if not job:
        return "Not found", 404
    return render_template("jobpage.html", job=job, company_name='Jovian',
                           year=year)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
