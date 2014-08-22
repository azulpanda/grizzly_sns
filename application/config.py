from application import app

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///sns_db?instance=grizzlyraccoon3:grizzlyraccoonsql3', 
    migration_directory = 'migrations'
))