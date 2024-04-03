#!/usr/bin/python3
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
engine = create_engine(
    f"mysql+mysqlconnector://{user}:{password}@{host}/{dbname}")
'''engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{dbname}")'''


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        keys = ['id', 'title', 'location', 'salary',
                'currency', 'responsibilities', 'requirements', 'application_deadline']
        for row_values in result.all():
            job_dict = dict(zip(keys, row_values))
            jobs.append(job_dict)
        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT * FROM jobs WHERE id = {id}"))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            keys = ['id', 'title', 'location', 'salary',
                    'currency', 'responsibilities', 'requirements', 'application_deadline']
            job = dict(zip(keys, rows[0]))
            return job


def add_application_to_db(job_id, data):
    try:
        with engine.connect() as conn:
            conn.execute(
                text("INSERT INTO applications (job_id, full_name, email,\
                    linkedin_url, education, work_experience, resume_url)\
                        VALUES (:job_id, :full_name, :email, :linkedin_url,\
                            :education, :work_experience, :resume_url)"),
                [{"job_id": job_id,
                  "full_name": data['full_name'],
                  "email": data['email'],
                  "linkedin_url": data['linkedin_url'],
                  "education": data['education'],
                  "work_experience": data['work_experience'],
                  "resume_url": data['resume_url']}]
            )
            conn.commit()
        return True
    except SQLAlchemyError as e:
        print(f"Error inserting data: {e}")
        return False
