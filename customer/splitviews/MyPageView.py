from .common import *

@login_required
def MyPageView(request):
    user = request.user

    like_bookSql = "SELECT isbn, book_name, book_img, store_id FROM book LEFT OUTER JOIN like_list on book.isbn = like_list.book_isbn " \
                   "LEFT OUTER JOIN bookstore on bookstore.id = like_list.store_id WHERE like_list.user_id = (%s)"

    book_datas = execute_and_get(like_bookSql,(user,))

    like_books = []
    for data in book_datas:
        bookstore = execute_and_get("SELECT store_name FROM bookstore WHERE id = (%s)", (data[3],))
        row = {'isbn': data[0],
                   'book_name': data[1],
                   'book_img': data[2],
                   'store_id': data[3],
                   'store_name': bookstore[0][0],
                   }
        like_books.append(row)


    favorite_storeSql = "SELECT a.bookstore_id, b.store_name, b.bookstore_img " \
                            "FROM favorite_bookstore as a " \
                            "JOIN bookstore as b " \
                            "ON a.bookstore_id = b.id " \
                            "where a.user_id=(%s) ORDER BY date desc"

    store_datas = execute_and_get(favorite_storeSql,(user,))

    favorite_stores = []
    for data in store_datas:
        row = {'store_id': data[0],
                   'store_name': data[1],
                   'store_img': data[2],
                   }
        favorite_stores.append(row)

    orderHistorySql = "SELECT a.buy_date, a.order_num, a.order_name, c.book_name, sum(b.quantity), sum(b.purchased_price), b.order_status " \
                      "FROM order_info as a " \
                      "JOIN order_products as b ON a.order_num = b.order_num " \
                      "JOIN book AS c ON b.isbn = c.isbn " \
                      "WHERE a.user_id = (%s) group by a.order_num order by buy_date desc"

    order_datas = execute_and_get(orderHistorySql,(user,))

    order_history = []
    for data in order_datas:
        row = {'buy_date': data[0],
               'order_num': data[1],
               'order_name': data[2],
               'book_name': data[3],
               'book_count': data[4],
               'sum_price': data[5],
               'order_status': data[6],
               }
        order_history.append(row)

    return render(request, 'mypage.html', {'like_books': like_books, 'favorite_stores': favorite_stores,
                                               'order_history': order_history})