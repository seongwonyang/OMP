from .common import *

def OrderReturnRejectView(request, return_id):
    product_id = execute_and_get("SELECT order_product_id FROM product_return WHERE id = (%s)", (return_id,))

    reject_reason = request.POST.get('reject_reason')

    execute("UPDATE product_return SET reject_reason = (%s) WHERE id = (%s)", (reject_reason, return_id,))
    execute("UPDATE order_products SET order_status = '반품 거절' WHERE id = (%s)", (product_id[0][0],))

    return redirect('seller:order_return')