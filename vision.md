# bolog API design

Just a collection of ideas, goals and constraints:

* the API should allow for CRUD operations on books
* the API should have two formats, JSON and protobuf, such that one is human readable and one is optimized.
* the database should be some form of document storage, so I'll most probably choose MongoDB.
* the whole thing should be secured by OAuth.
