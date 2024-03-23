from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Accra, Ghana',
        'salary': 'GHS 4000'
    },
    {
        'id': 2,
        'title': 'Software Developer',
        'location': 'Kumasi, Ghana',
        'salary': 'GHS 6500'
    },
    {
        'id': 3,
        'title': 'Softwae Engineer',
        'location': 'Remote',
        'salary': 'GHS 8000'
    },
    {
        'id': 4,
        'title': 'Data Entry Clerk',
        'location': 'Sunyani, Ghana',
        'salary': 'GHS 1500'
    },
    {
        'id': 5,
        'title': "Miriam Tagoe's TA",
        'location': 'Miotso, Ghana',
        'salary': 'GHS 1800'
    }
    ,
    {
        'id': 6,
        'title': "Ekua Thompson's Lab Assistant",
        'location': 'Ho, Ghana',
        'salary': 'GHS 1800'
    },
    {
        'id': 7,
        'title': "Assistant to the Executive Assistant",
        'location': 'Appolonia City, Ghana',
        'salary': 'GHS 2400'
    }
]

@app.route('/', strict_slashes=False)
def hello_world():
    return render_template("home.html", jobs=JOBS)

@app.route('/jobs', strict_slashes=False)
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)