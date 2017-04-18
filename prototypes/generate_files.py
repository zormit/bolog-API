import json

books = json.load(open("books_by_isbn.json", "r"))
for isbn, book in books.items():
    json.dump(book, open("data/{}.json".format(isbn), "w"))
