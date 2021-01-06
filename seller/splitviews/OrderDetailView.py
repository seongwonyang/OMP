from .common import *

@login_required
def OrderDetailView(request, order_num):
    user = request.user

    store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    order_products = execute_and_get("SELECT isbn, quantity FROM order_products WHERE order_num = (%s) AND store_id = (%s)", (order_num, store_id[0][0],))

    order_info = execute_and_get("SELECT order_name, order_address, order_p_num, order_email, order_memo " +
                                 "FROM order_info WHERE order_num = (%s)", (order_num,))

    book_data = []
    for order_product in order_products:
        book_info = execute_and_get("SELECT book_name, author, publisher, book_img FROM book WHERE isbn = (%s)", (order_product[0],))
        row = {'isbn': order_product[0],
               'quantity': order_product[1],
               'book_name': book_info[0][0],
               'author': book_info[0][1],
               'publisher': book_info[0][2],
               'book_img': book_info[0][3]
               }

        book_data.append(row)

    order_detail = {'order_name': order_info[0][0],
                    'order_address': order_info[0][1],
                    'order_p_num': order_info[0][2],
                    'order_email': order_info[0][3],
                    'order_memo': order_info[0][4],
                    }

    return HttpResponse(json.dumps({'order_detail': order_detail, 'book_data': book_data}), content_type="application/json")