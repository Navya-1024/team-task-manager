from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import os

if not os.path.exists("database.db"):
    open("database.db", "w").close()
users = []
projects = []
tasks = []
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print("DB error:", e)
# ---------------- DATABASE ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(20))

    # -------- PROJECT TABLE --------
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    created_by = db.Column(db.Integer)

# -------- TASK TABLE --------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    status = db.Column(db.String(20), default="Pending")
    assigned_to = db.Column(db.Integer)
    project_id = db.Column(db.Integer)

# ---------------- ROUTES ----------------

@app.route('/')
def home():
    return redirect('/login')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return redirect('/login')
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            return redirect('/dashboard')
        else:
            return "Invalid username or password"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    tasks = Task.query.all()

    total = len(tasks)
    completed = len([t for t in tasks if t.status == "Completed"])
    pending = len([t for t in tasks if t.status == "Pending"])

    return render_template('dashboard.html',
                           total=total,
                           completed=completed,
                           pending=pending,
                           tasks=tasks)

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        name = request.form['name']

        project = Project(name=name, created_by=1)
        db.session.add(project)
        db.session.commit()

        return redirect('/dashboard')

    return render_template('create_project.html')

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    users = User.query.all()
    projects = Project.query.all()

    if request.method == 'POST':
        title = request.form['title']
        assigned_to = request.form['assigned_to']
        project_id = request.form['project_id']

        task = Task(title=title,
                    assigned_to=assigned_to,
                    project_id=project_id)

        db.session.add(task)
        db.session.commit()

        return redirect('/dashboard')

    return render_template('create_task.html',
                           users=users,
                           projects=projects)

@app.route('/complete/<int:id>')
def complete_task(id):
    task = Task.query.get(id)
    task.status = "Completed"
    db.session.commit()

    return redirect('/dashboard')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
