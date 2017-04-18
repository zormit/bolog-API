var options = {
  valueNames: [ 'title', 'authors', 'shelf' ],
  // Since there are no elements in the list, this will be used as template.
  item: '<tr><td class="title"></td><td class="authors"></td><td class="shelf"></td></tr>'
};

var bookList = new List('books', options, books);

/*bookList.add({
  title: 'Gustaf Lindqvist',
  author: 1983
}); */
