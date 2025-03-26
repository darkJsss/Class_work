from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.hashed_password = "12e1314"
    user.email = "scott_chief@mars.org"
    user1 = User()
    user1.surname = "Scott1"
    user1.name = "Ridley1"
    user1.age = 21
    user1.position = "captain1"
    user1.speciality = "research engineer1"
    user1.address = "module_1_1"
    user1.email = "scott_chif@mars1.org"
    user2 = User()
    user2.surname = "Scott2"
    user2.age = 21
    user2.name = "Ridley2"
    user2.position = "captain2"
    user2.speciality = "research engineer2"
    user2.address = "module_1_2"
    user2.email = "scot_chief@mars2.org"
    user3 = User()
    user3.surname = "Scott3"
    user3.name = "Ridley3"
    user3.age = 21
    user3.position = "captain3"
    user3.speciality = "research engineer3"
    user3.address = "module_1_3"
    user3.email = "scotttt_chief@mars3.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
