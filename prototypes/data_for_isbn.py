import requests
import json
from pprint import pprint

API_KEY = open('api.key').readline().strip()
API_URL_FORMAT = 'http://isbndb.com/api/v2/json/{api_key}/book/{isbn}'

if __name__ == '__main__':
    category = input("which category? ").strip()
    topic = input("which topic? ").strip()
    shelf = input("which shelf (e.g. 5.1)? ").strip()
    while True:
        # scan isbns
        isbn = input("enter isbn: ").strip()
        if isbn == '':
            continue
        print("fetching data for {}".format(isbn))

        url = API_URL_FORMAT.format(api_key=API_KEY, isbn=isbn)
        res = requests.get(url)

        data = res.json()
        if 'data' in data:
            assert len(data['data']) == 1, "the book endpoint should only return one book"
            book = data['data'][0]
            book['category'] = category
            book['topic'] = topic
            book['shelf'] = shelf

            keys = ['author_data', 'title', 'title_long', 'isbn10', 'isbn13']
            pprint({key: val for key, val in book.items() if key in keys})
            while True:
                yesno = input("add this book? [Y/n]")
                if yesno == '' or yesno.lower() == 'y':
                    store = True
                    break
                elif yesno.lower() == 'n':
                    store = False
                    break
                print("say again...")

            if store:
                with open("books.jsonl", "a") as collect_books:
                    collect_books.write(json.dumps(book) + '\n')
        elif 'error' in data:
            print("the API returned the following error: {}".format(data['error']))
            book = {}
            book['isbn'] = isbn
            book['category'] = category
            book['topic'] = topic
            book['shelf'] = shelf
            book['error'] = data['error']

            with open("notfounds.jsonl", "a") as notfound_books:
                notfound_books.write(json.dumps(book) + '\n')
        else:
            print("The response format is not as expected.")
