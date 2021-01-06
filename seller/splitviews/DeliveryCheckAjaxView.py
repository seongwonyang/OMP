from .common import *

@login_required
def DeliveryCheckAjaxView(request, order_num):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))

    select_status_sql = "SELECT order_status FROM order_products WHERE order_num = (%s) and store_id = (%s)"
    order_status = execute_and_get(select_status_sql, (order_num, store_id[0][0],))

    if order_status[0][0] == "결제 완료":
        update_sql = "UPDATE order_products SET order_status = '배송 준비' WHERE order_num = (%s) and store_id = (%s)"
        execute(update_sql, (order_num, store_id[0][0],))
    elif order_status[0][0] == "배송 준비":
        update_sql = "UPDATE order_products SET order_status = '배송 중' WHERE order_num = (%s) and store_id = (%s)"
        execute(update_sql, (order_num, store_id[0][0],))

    select_update_status_sql = "SELECT order_status FROM order_products WHERE order_num = (%s) and store_id = (%s)"
    update_order_status = execute_and_get(select_update_status_sql, (order_num, store_id[0][0],))

    return HttpResponse(json.dumps({'update_order_status': update_order_status[0][0]}), content_type="application/json")