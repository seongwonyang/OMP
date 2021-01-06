from .common import *

def OrderSheetView (request, book_isbn, store_id):

    quantity = request.POST.get('quantity')

    bookSql = "SELECT a.book_name, a.book_img, c.store_name " \
                  "FROM book AS a " \
                  "JOIN book_inven AS b " \
                  "ON a.isbn = b.book_isbn " \
                  "JOIN bookstore AS c " \
                  "ON b.store_id = c.id " \
                  "where a.isbn = (%s) and b.store_id = (%s)"

    data = execute_and_get(bookSql, (book_isbn, store_id,))
    price = execute_and_get("SELECT price FROM book_inven WHERE book_isbn = (%s) AND store_id = (%s)", (book_isbn, store_id,))

    goods = {'book_name': data[0][0],
                 'price': price[0][0],
                 'book_img': data[0][1],
                 'store_name':data[0][2],
                 'quantity': quantity,
                 }

    total_price = price[0][0]*int(quantity)

    return render(request, 'order_sheet.html',{'goods':goods,'total_price': total_price})