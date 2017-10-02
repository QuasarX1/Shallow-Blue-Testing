import unittest
from app import *

class Test_dbTest(unittest.TestCase):
    def startUp(self):
        
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_setup(self):
        
        with app.app_context():

            addEvent("eventName", datetime.datetime.now(), "info")

if __name__ == '__main__':
    unittest.main()
