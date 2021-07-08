# instance/config.py

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://dt_admin:dt2016@localhost/dreamteam_db'.format(user='dt_admin', password='dt2016', server='localhost', database='dreamteam_db')
