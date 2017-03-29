from flask import Blueprint
from voluptuous import Schema, Required, Any, REMOVE_EXTRA
from six import string_types

from bolog.api_components import ApiResult, dataschema

books = Blueprint('books', __name__)


@books.route("/json/books")
def list_books():
    # TODO: fetch data from the DB
    return ApiResult([])


@books.route("/json/book", methods=["POST"])
@dataschema(Schema({
    Required('title'): Any(*string_types),
    Required('authors'): list,  # TODO: of strings
    # 'category': Any(*string_types),
    # 'topic': Any(*string_types),
}, extra=REMOVE_EXTRA))
def add_book(title, authors, category=None, topic=None):
    # TODO actually add the book :)
    return ApiResult(None)
