import sqlalchemy

db = sqlalchemy.create_engine('sqlite:///tutorial.db')

db.echo = True

user_table = sqlalchemy.Table('users',
                              sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True))
