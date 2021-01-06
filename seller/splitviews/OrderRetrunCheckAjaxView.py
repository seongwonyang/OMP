from .common import *

def OrderReturnCheckAjaxView(request, return_id):
    order_product_id = execute_and_get("SELECT order_product_id FROM product_return WHERE id = (%s)", (return_id,))

    order_status = execute_and_get("SELECT order_status FROM order_products WHERE id = (%s)", (order_product_id[0][0],))

    if order_status[0][0] == "반품 접수중":
        execute("UPDATE order_products SET order_status = '반품 처리중' WHERE id = (%s)", (order_product_id[0][0],))
    elif order_status[0][0] == "반품 처리중":
        execute("UPDATE order_products SET order_status = '반품 접수중' WHERE id = (%s)", (order_product_id[0][0],))

    update_return_status = execute_and_get("SELECT order_status FROM order_products WHERE id = (%s)", (order_product_id[0][0],))

    return HttpResponse(json.dumps({'update_return_status': update_return_status[0][0]}), content_type="application/json")