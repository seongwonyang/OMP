from .common import *

def MainView (request):

    bookSql = "SELECT book_name, book_img, isbn FROM book as a " \
                "JOIN like_list as b " \
                "on a.isbn = b.book_isbn " \
                "WHERE date BETWEEN DATE_ADD(NOW(),INTERVAL -1 WEEK ) AND NOW() " \
                "group by book_isbn ORDER BY count(book_isbn) desc limit 3"

    storeSql = "SELECT store_name, store_msg, a.id FROM bookstore as a " \
                "JOIN favorite_bookstore as b " \
                "on a.id = b.bookstore_id " \
                "WHERE date BETWEEN DATE_ADD(NOW(),INTERVAL -1 WEEK ) AND NOW() " \
                "group by bookstore_id ORDER BY count(bookstore_id) desc"

    datas = execute_and_get(bookSql)

    datas2 = execute_and_get(storeSql)

    books = []
    for data in datas:
        row = {'book_name':data[0],
               'book_img':data[1],
               'isbn':data[2],
               }
        books.append(row)

    stores = []
    for data in datas2:
        row = {'store_name': data[0],
               'store_msg': data[1],
               'store_id':data[2],
               }
        stores.append(row)

    return render(request, 'main.html',{'books':books, 'stores':stores})