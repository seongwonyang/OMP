from .common import *

def BookStoreDetailView (request, store_id):
    user = request.user

    storeSql = "SELECT store_name, address, store_num, bookstore_img, store_msg, id FROM bookstore where id =(%s)"

    data = execute_and_get(storeSql,(store_id,))

    store = {'store_name': data[0][0],
             'address': data[0][1],
             'store_num': data[0][2],
             'store_img': data[0][3],
             'store_msg': data[0][4],
             'store_id':data[0][5],
            }

    favoriteSql = "SELECT EXISTS (SELECT id FROM favorite_bookstore WHERE bookstore_id=(%s) AND user_id=(%s))"

    favorite_data = execute_and_get(favoriteSql, (store_id,user.username,))

    is_favorite = favorite_data[0][0]

    bookSql =  "SELECT a.isbn, a.book_name, b.price, a.book_img, b.store_id, a.author " \
               "FROM book AS a " \
               "JOIN book_inven AS b " \
               "ON a.isbn = b.book_isbn " \
               "where store_id = (%s)"

    datas = execute_and_get(bookSql,(store_id,))

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            'store_id':data[4],
            'author': data[5],
            }
        books.append(row)

    like_bookSql = "SELECT b.book_isbn, b.book_name, b.price, a.book_img, b.store_id, a.author " \
                   "FROM book AS a " \
                   "JOIN book_inven AS b " \
                   "ON a.isbn = b.book_isbn " \
                   "JOIN like_list as c " \
                   "on b.book_isbn = c.book_isbn " \
                   "where c.store_id = (%s) " \
                   "group by c.book_isbn ORDER BY count(c.book_isbn) desc limit 3"

    datas = execute_and_get(like_bookSql, (store_id,))

    like_books = []
    for data in datas:
        row = {
            'isbn': data[0],
            'book_name': data[1],
            'price': data[2],
            'book_img': data[3],
            'store_id': data[4],
            'author': data[5],
        }
        like_books.append(row)

    lately_bookSql =  "SELECT b.book_isbn, b.book_name, b.price, a.book_img, b.store_id, a.author " \
                      "FROM book AS a " \
                      "JOIN book_inven AS b " \
                      "ON a.isbn = b.book_isbn " \
                      "where store_id = (%s) " \
                      "ORDER BY b.time desc limit 3"

    datas = execute_and_get(lately_bookSql,(store_id,))

    lately_books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            'store_id':data[4],
            'author': data[5],
            }
        lately_books.append(row)

    notice_sql = "SELECT notice, date FROM notice WHERE store_id = (%s) ORDER BY date desc limit 3"

    datas = execute_and_get(notice_sql,(store_id,))

    notices = []
    for data in datas:
        row = {
            'notice':data[0],
            'date':data[1],
            }
        notices.append(row)

    return render(request, 'bookstore_detail.html',{'store':store, 'is_favorite':is_favorite,
                                                    'books':books, 'like_books':like_books, 'lately_books':lately_books,
                                                    'notices':notices})