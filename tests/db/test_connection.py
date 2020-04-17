from flask_mongoengine import MongoEngine

def test_connection():
    """
      Test that aur flask_mongoengine(mapper) is connected to mongodb or not
    """
    from app.settings.extensions import db
    assert isinstance(db, MongoEngine)

def test_invalid_connect():
    from app.settings.extensions import db
    assert not isinstance(None, MongoEngine)
