from .common import *

@login_required
def SearchBookInManageView (request):
    tab = 'search_book'
    user = request.user
    search_book = request.POST.get('search_book')
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))

    book_sql = "SELECT a.isbn, a.book_name, b.price, a.book_img, b.store_id, a.author, b.inven " \
               "FROM book AS a " \
               "JOIN book_inven AS b " \
               "ON a.isbn = b.book_isbn " \
               "WHERE b.store_id = (%s) and (a.book_name LIKE '%%" + search_book + "%%' or a.author LIKE '%%" + search_book + "%%') GROUP BY a.book_name"

    datas = execute_and_get(book_sql, (store_id[0][0],))

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'price':data[2],
            'book_img':data[3],
            'store_id':data[4],
            'author': data[5],
            'quantity':data[6],
            }
        books.append(row)

    if search_book == "":
        messages.error(request, '검색 키워드를 하나 이상 입력해주세요')
        return redirect('seller:product_list')

    return render(request, 'product_manage.html', {'tab':tab,'books':books,'search_book':search_book})