import os
import bolog
import unittest
import json

class BologTestCase(unittest.TestCase):

    def setUp(self):
        bolog.app.config['TESTING'] = True
        self.app = bolog.app.test_client()
        #with bolog.app.app_context():
        #    bolog.init_db()

    def test_empty_db(self):
        rv = self.app.get('/json/books')
        rv = json.loads(rv.data.decode('utf-8'))
        assert len(rv) == 0

    def test_insert_correct_formatted_book(self):
        book = {"title": "my way to reading", "authors": ["me", "somebody else"]}
        rv = self.app.post('/json/book', data=json.dumps(book), content_type='application/json')
        assert rv.status_code == 200

    def test_insert_wrongly_formatted_book(self):
        book = {"title": "my way to reading"}
        rv = self.app.post('/json/book', data=json.dumps(book), content_type='application/json')
        assert rv.status_code == 400 # bad request

if __name__ == '__main__':
    unittest.main()
