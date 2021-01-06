from .common import *

def PayCheckAjaxView(request, order_num):
    user = request.user

    store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s) AND store_id = (%s)", (order_num, store_id[0][0]))

    if order_status[0][0] == "결제 대기중":
        execute("UPDATE order_products SET order_status = '결제 완료' WHERE order_num = (%s) AND store_id = (%s)", (order_num, store_id[0][0]))
        inven_sql = "UPDATE book_inven A INNER JOIN order_products B " \
                    "ON A.book_isbn = B.isbn SET inven = inven-quantity " \
                    "WHERE A.store_id = (%s) and order_num = (%s)"
        execute(inven_sql, (store_id[0][0], order_num,))

    else:
        execute("UPDATE order_products SET order_status = '결제 대기중' WHERE order_num = (%s) AND store_id = (%s)", (order_num, store_id[0][0]))
        inven_sql = "UPDATE book_inven A INNER JOIN order_products B " \
                    "ON A.book_isbn = B.isbn SET inven = inven+quantity " \
                    "WHERE A.store_id = (%s) and order_num = (%s)"
        execute(inven_sql, (store_id[0][0], order_num,))

    update_order_status = execute_and_get("SELECT order_status FROM order_products WHERE order_num = (%s) AND store_id = (%s)", (order_num, store_id[0][0]))

    return HttpResponse(json.dumps({'update_order_status': update_order_status[0][0]}), content_type="application/json")