from base_fixtures import BaseFixtures

import json


class TestBooks(BaseFixtures):
    # these are currently in the form of "integration tests"

    def test_empty_db(self, test_client):
        rv = test_client.get('/json/books')
        data = json.loads(rv.data.decode('utf-8'))
        assert len(data) == 0

    def test_insert_correct_formatted_book(self, test_client):
        book = {"title": "my way to reading", "authors": ["me", "somebody else"]}
        rv = test_client.post('/json/book', data=json.dumps(book),
                              content_type='application/json')
        assert rv.status_code == 200

    def test_insert_wrongly_formatted_book(self, test_client):
        book = {"title": "my way to reading"}
        rv = test_client.post('/json/book',
                              data=json.dumps(book),
                              content_type='application/json')
        data = json.loads(rv.data.decode('utf-8'))
        assert rv.status_code == 400
        assert 'message' in data
        assert 'Invalid data' in data.get('message')
        assert 'authors' in data.get('message')
