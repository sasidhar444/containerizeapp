from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index.html')
def homepage2():
    return render_template('index.html')

@app.route('/about.html')
def aboutpage():
    return render_template('about.html')

@app.route('/components.html')
def componentspage():
    return render_template('components.html')

@app.route('/project.html')
def projectspage():
    return render_template('project.html')

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5000, debug = True)