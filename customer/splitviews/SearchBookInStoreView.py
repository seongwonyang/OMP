from .common import *

def SearchBookInStoreView (request):
    tab = 'search_book'
    user = request.user
    search_book = request.POST.get('search_book')
    store_id = request.POST.get('store_id')

    storeSql = "SELECT store_name, address, phone_num, bookstore_img, store_msg, id FROM bookstore where id =(%s)"

    data = execute_and_get(storeSql, (store_id,))

    store = {'store_name': data[0][0],
             'address': data[0][1],
             'phone_num': data[0][2],
             'store_img': data[0][3],
             'store_msg': data[0][4],
             'store_id': data[0][5],
             }

    favoriteSql = "SELECT EXISTS (SELECT id FROM favorite_bookstore WHERE bookstore_id=(%s) AND user_id=(%s))"

    favorite_data = execute_and_get(favoriteSql, (store_id, user.username,))

    is_favorite = favorite_data[0][0]

    bookSql = "SELECT a.book_isbn, a.book_name, a.price, b.book_img, b.author, a.store_id " \
              "FROM book_inven as a JOIN book as b on a.book_isbn = b.isbn " \
              "WHERE a.store_id = (%s) and (a.book_name LIKE '%%" + search_book + "%%' or b.author LIKE '%%" + search_book + "%%') GROUP BY a.book_name"

    datas = execute_and_get(bookSql, (store_id,))

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            'author':data[4],
            'store_id':data[5],
            }
        books.append(row)

    if search_book == "":
        messages.error(request, '검색 키워드를 하나 이상 입력해주세요')
        return redirect('customer:bookstore_detail', store_id)

    notice_sql = "SELECT notice, date FROM omp3.notice WHERE store_id = (%s) ORDER BY date desc limit 3"

    datas = execute_and_get(notice_sql,(store_id,))

    notices = []
    for data in datas:
        row = {
            'notice':data[0],
            'date':data[1],
            }
        notices.append(row)

    return render(request, 'bookstore_detail.html', {'tab':tab,'books':books,'search_book':search_book,
                                                     'store':store, 'is_favorite':is_favorite,'notices':notices})