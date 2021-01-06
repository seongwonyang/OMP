from .common import *

@login_required
def AjaxGetProductInfoView(request, isbn):
    user = request.user
    idSql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(idSql, (user,))

    book_sql = "SELECT book_name, inven, price, book_msg " \
               "FROM book_inven WHERE store_id=(%s) and book_isbn=(%s) "
    data = execute_and_get(book_sql, (store_id[0][0], isbn,))

    book_info = {'name': data[0][0],
                 'inven': data[0][1],
                 'price': data[0][2],
                 'book_msg': data[0][3],
                 'store_id': store_id[0][0],
                 'isbn': isbn,}

    return HttpResponse(json.dumps({'book_info': book_info}), content_type="application/json")