#!/usr/bin/python3
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

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