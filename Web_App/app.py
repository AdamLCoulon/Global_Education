from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about_project')
def aboutpage():
    return render_template('aboutpage.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/spending')
def spending():
    return render_template('spending.html')

@app.route('/education_levels')
def educationlevels():
    return render_template('educationlevels.html')

@app.route('/education_future')
def educationfuture():
    return render_template('educationfuture.html')
