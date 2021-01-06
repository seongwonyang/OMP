from .common import *

# 반품 관리를 신규, 완료, 전체 세 가지 중, 어떤 방법으로 요청하는지에 따라 'click_case'로 분기
def OrderReturnView(requet, click_case):
    user = requet.user

    store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    return_product = ()
    if click_case == 'all':
        datas = execute_and_get("SELECT b.user_id, b.order_product_id, b.return_reason, b.product_img, " +
                                     "a.delivery_compl_time, a.order_num, a.purchased_price, b.id, a.order_status, b.time, b.return_complete " +
                                     "FROM order_products as a JOIN product_return as b ON a.id = b.order_product_id "+
                                     "WHERE a.store_id = (%s) ORDER BY time DESC", (store_id[0][0],))
        return_product += datas

    elif click_case == 'new':
        datas = execute_and_get("SELECT b.user_id, b.order_product_id, b.return_reason, b.product_img, " +
                                         "a.delivery_compl_time, a.order_num, a.purchased_price, b.id, a.order_status, b.time, b.return_complete " +
                                         "FROM order_products as a JOIN product_return as b ON a.id = b.order_product_id " +
                                         "WHERE a.store_id = (%s) AND a.order_status = (%s) ORDER BY time DESC",
                                         (store_id[0][0], '반품 접수중',))
        return_product += datas

    elif click_case == 'complete':
        datas = execute_and_get("SELECT b.user_id, b.order_product_id, b.return_reason, b.product_img, " +
                                         "a.delivery_compl_time, a.order_num, a.purchased_price, b.id, a.order_status, b.time, b.return_complete " +
                                         "FROM order_products as a JOIN product_return as b ON a.id = b.order_product_id " +
                                         "WHERE a.store_id = (%s) AND a.order_status = (%s) ORDER BY time DESC",
                                         (store_id[0][0], '반품 완료',))
        return_product += datas

    products = []
    for data in return_product:
        user_name = execute_and_get("SELECT order_name FROM order_info WHERE user_id = (%s)", (data[0],))
        row = {'user_id': data[0],
               'user_name': user_name[0][0],
               'return_reason': data[2],
               'product_img': data[3],
               'delivery_compl_time': data[4],
               'order_num': data[5],
               'purchased_price': data[6],
               'return_id': data[7],
               'order_status': data[8],
               'time': data[9],
               'return_complete': data[10],
               }

        products.append(row)

    return render(requet, "order_return.html", {'products': products})