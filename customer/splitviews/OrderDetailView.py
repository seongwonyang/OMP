from .common import *

@login_required
def OrderDetailView(request,order_num):
    order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s)", (order_num,))

    orderDetailSql = "SELECT a.order_num, b.first_name, a.order_name, a.order_address, " \
                     "a.order_p_num, a.order_memo, a.payment, sum(c.purchased_price), a.buy_date, " \
                     "CASE WHEN a.payment = 'bank' THEN date_add(a.buy_date,INTERVAL 1 DAY) ELSE null END AS due_date " \
                     "FROM order_info as a JOIN customer_accounts_user as b ON a.user_id = b.username " \
                     "JOIN order_products as c ON a.order_num = c.order_num where a.order_num = (%s)"

    data = execute_and_get(orderDetailSql,(order_num,))

    order_detail = {'order_num': data[0][0],
                    'user_name':data[0][1],
                    'order_name':data[0][2],
                    'order_address':data[0][3],
                    'order_p_num':data[0][4],
                    'order_memo':data[0][5],
                    'payment':data[0][6],
                    'price':data[0][7],
                    'buy_date':data[0][8],
                    'due_date':data[0][9],
                    }

    productSql = "SELECT a.book_name, c.store_name, b.purchased_price, a.book_img, b.order_status, b.quantity, b.id " \
                 "FROM book AS a " \
                 "JOIN order_products AS b " \
                 "ON a.isbn = b.isbn " \
                 "JOIN bookstore AS c " \
                 "ON b.store_id = c.id " \
                 "where order_num = (%s)"

    datas = execute_and_get(productSql, (order_num,))

    products = []
    for data in datas:
        price = execute_and_get("SELECT price FROM book_inven WHERE book_isbn = (%s) AND store_id = (%s)",
                                (data[4], data[5],))

        return_possible = execute_and_get("SELECT return_possible FROM order_products WHERE id = (%s)",
                                          (data[6],))

        row = {
            'book_name': data[0],
            'store_name': data[1],
            'price': data[2],
            'book_img': data[3],
            'order_status':data[4],
            'quantity':data[5],
            'order_product_id': data[6],
            'return_possible': return_possible[0][0]
        }
        products.append(row)

    accountSql = "SELECT c.store_name, sum(a.purchased_price), b.account, b.bank " \
                 "FROM order_products AS a " \
                 "JOIN shipping_info AS b ON a.store_id = b.bookstore_id " \
                 "JOIN bookstore AS c ON a.store_id = c.id " \
                 "WHERE order_num = (%s) GROUP BY store_id"

    account_datas = execute_and_get(accountSql, (order_num,))

    account_info = []
    for data in account_datas:
        row = {
            'store_name': data[0],
            'price': data[1],
            'account': data[2],
            'bank': data[3],
        }
        account_info.append(row)

    return_reject_datas = \
        execute_and_get("SELECT a.reject_reason, b.isbn " +
                        "FROM product_return as a JOIN order_products as b ON a.order_product_id = b.id " +
                        "WHERE b.order_num = (%s)", (order_num,))

    return_reject_info = []
    for data in return_reject_datas:
        book_name = execute_and_get("SELECT book_name FROM book WHERE isbn = (%s)", (data[1],))
        row = {
            'reject_reason': data[0],
            'book_name': book_name[0][0],
        }
        return_reject_info.append(row)

    is_return_reject = 0
    if len(return_reject_info) != 0:
        is_return_reject = 1

    return render(request, 'order_detail.html', {'order_detail':order_detail, 'products':products,
                                                 'account_info':account_info, 'order_status':order_status[0][0], 'return_reject_info': return_reject_info,
                                                 'is_return_reject': is_return_reject})