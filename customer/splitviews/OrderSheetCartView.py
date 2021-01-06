from .common import *

def OrderSheetCartView (request):
    if request.method == 'POST':
        tab = 'basket'
        checked_cart = request.POST.getlist('cart')
        bookSql = "SELECT a.book_name, b.price, a.book_img, c.store_name " \
                  "FROM book AS a " \
                  "JOIN book_inven AS b " \
                  "ON a.isbn = b.book_isbn " \
                  "JOIN bookstore AS c " \
                  "ON b.store_id = c.id " \
                  "where a.isbn = (%s) and b.store_id = (%s)"

        carts = []
        total_price = 0
        for cart in checked_cart:
            cart = cart.split(",")
            store_id = cart[0]
            isbn = cart[1]
            quantity = cart[2]
            datas = execute_and_get(bookSql, (isbn, store_id,))
            row = {'book_name': datas[0][0],
                       'price': datas[0][1],
                       'book_img': datas[0][2],
                       'store_name': datas[0][3],
                       'quantity':quantity,
                       }
            carts.append(row)
            total_price += datas[0][1]*int(quantity)

    return render(request,'order_sheet.html',{'carts':carts,
                                              'tab': tab, 'total_price': total_price})