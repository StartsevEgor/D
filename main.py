from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, render_template, redirect, request, abort, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


@app.route("/")
def index():
    print(1)
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    print(2, url_for("static", filename='css/style.css'))
    return render_template('static/templates/index.html', jobs=jobs)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


if __name__ == '__main__':
    main()
