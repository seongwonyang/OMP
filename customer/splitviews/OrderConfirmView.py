from .common import *

@login_required

def OrderConfirmView (request, order_num):

    infoSql = "SELECT order_name, order_p_num, order_address, order_num " \
                  "FROM order_info where order_num = (%s)"

    data = execute_and_get(infoSql,(order_num,))

    info = {'order_name': data[0][0],
            'order_p_num': data[0][1],
            'order_address': data[0][2],
            'order_num':data[0][3],
            }

    productSql = "SELECT a.book_name, c.store_name, a.price, a.book_img " \
                 "FROM book AS a " \
                 "JOIN order_products AS b " \
                 "ON a.isbn = b.isbn " \
                 "JOIN bookstore AS c " \
                 "ON b.store_id = c.id " \
                 "where order_num = (%s)"

    datas = execute_and_get(productSql,(order_num,))

    products = []
    for data in datas:
        row = {
            'book_name':data[0],
            'store_name':data[1],
            'price':data[2],
            'book_img':data[3],
            }
        products.append(row)

    paymentSql = "SELECT payment, date_add(buy_date,INTERVAL 1 DAY) FROM order_info where order_num = (%s)"

    data = execute_and_get(paymentSql, (order_num,))
    payment = {'payment': data[0][0],
               'due_date': data[0][1],
               }

    accountSql = "SELECT c.store_name, sum(a.price), b.account " \
                 "FROM order_products AS a " \
                 "JOIN shipping_info AS b ON a.store_id = b.bookstore_id " \
                 "JOIN bookstore AS c ON a.store_id = c.id " \
                 "WHERE order_num = (%s) GROUP BY store_id"

    account_datas = execute_and_get(accountSql, (order_num,))

    account_info = []
    for data in account_datas:
        row = {
            'store_name':data[0],
            'price':data[1],
            'account':data[2],
            }
        account_info.append(row)

    return render(request, 'order_confirm.html', {'info': info, 'products':products,
                                                  'payment':payment, 'account_info':account_info})