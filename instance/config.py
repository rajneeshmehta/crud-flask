# instance/config.py

SECRET_KEY = 'p9Bv<3Eid9%$i01'
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://flask-app:LessSecretPassword@172.17.0.6/employee'.format(user='flask-app', password='LessSecretPassword', server='172.17.0.6', database='employee')
