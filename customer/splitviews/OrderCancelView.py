from .common import *

@login_required
def OrderCancelView(request, order_num):
    execute("UPDATE order_products SET order_status = '결제취소' WHERE order_num = (%s)", (order_num,))

    return redirect("customer:mypage")