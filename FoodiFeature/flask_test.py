from FoodiFeature import foodiFeature
import flask
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        flask.app.testing = True
        self.app = foodiFeature.app.test_client()

    def tearDown(self):
        pass

    def test_working(self):
        rv = self.app.get('/')
        print(rv.data)
        assert b'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main()
