from .common import *

def OrderReturnRejectCompAjaxlView(request, return_id):
    return_info = execute_and_get("SELECT order_product_id, return_complete FROM product_return WHERE id = (%s)", (return_id,))

    if return_info[0][1] == 0:
        execute("UPDATE product_return SET return_complete = 1 WHERE id = (%s)", (return_id,))
        execute("UPDATE order_products SET order_status = '반품 완료' WHERE id = (%s)", (return_info[0][0],))
    elif return_info[0][1] == 1:
        execute("UPDATE product_return SET return_complete = 0 WHERE id = (%s)", (return_id,))
        execute("UPDATE order_products SET order_status = '반품 처리중' WHERE id = (%s)", (return_info[0][0],))

    update_return_complete = execute_and_get("SELECT return_complete FROM product_return WHERE id = (%s)", (return_id,))

    return HttpResponse(json.dumps({'update_return_complete': update_return_complete[0][0]}), content_type="application/json")