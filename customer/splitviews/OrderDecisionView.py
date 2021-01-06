from .common import *

@login_required
def OrderDecisionView(request, order_num):
    execute("UPDATE order_products SET order_status = '구매확정', settlement = '구매확정' WHERE order_num = (%s) AND order_status = (%s)",
            (order_num, "배송 완료"))

    return redirect("customer:mypage")