#import pdb
import unittest
import os
from app import app
from database import db_session
from models import Items


class TestItems(unittest.TestCase):
    def setUp(self):
        #app = Flask(__name__)
	#app.secret_key = os.environ['APP_SECRET_KEY']
        app.config.from_object('app.config.Testing')
        db_session.close()
        db_session.drop_all()
        db_session.create_all()

    def test_fill(self):
        item = Items(name="test", quantity=1, description="test", date_added=datetime.datetime.now())
        db_session.add(item)
        db_session.commit()
        items = Items.query.all()
        assert item in items
        print len(items)
