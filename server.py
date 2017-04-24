from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE


@app.route('/')
def index():
    """Return homepage"""

    return render_template("index.html")

@app.route('/application-form')
def application_form():
    """Return page with application form"""


    return render_template('application-form.html', jobs=["Software Engineer", "QA Engineer", "Product Manager"])

@app.route('/application-success', methods=['POST'])
def application_success():
    """Return page with application response"""

    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    salary = request.form.get('salary')
    job = request.form.get('choice')
    salary = float(salary)

    return render_template('application-response.html', fname=first_name, lname=last_name, salary=salary, job=job)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
