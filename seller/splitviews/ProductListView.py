from .common import *

@login_required
def ProductListView (request):
    user = request.user
    idSql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(idSql, (user,))

    bookSql =  "SELECT a.isbn, a.book_name, b.price, a.book_img, b.store_id, a.author, b.inven " \
               "FROM book AS a " \
               "JOIN book_inven AS b " \
               "ON a.isbn = b.book_isbn " \
               "where store_id = (%s)"

    datas = execute_and_get(bookSql,(store_id[0][0],))

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

    return render(request, 'product_manage.html',{'books':books})