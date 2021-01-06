from .common import *

@login_required
def OrderCheckView(request):
    user = request.user

    seller_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id=(%s)", (user.username,))

    order_datas = execute_and_get("SELECT DISTINCT order_num, order_status FROM order_products WHERE store_id = (%s) AND order_status = (%s)",
                                  (seller_id[0][0], "결제 대기중",))

    order_info_list = []
    for order_data in order_datas:
        buyer_data = execute_and_get("SELECT payment, buy_date FROM order_info WHERE order_num = (%s)", (order_data[0],))
        total_price = execute_and_get("SELECT SUM(purchased_price) FROM order_products WHERE order_num = (%s)", (order_data[0],))

        row = {'order_num': order_data[0],
               'order_status': order_data[1],
               'purchased_price': total_price[0][0],
               'buy_date': buyer_data[0][1],
               'payment': buyer_data[0][0]}

        order_info_list.append(row)

    return render(request, 'order_check.html', {'order_info_list': order_info_list})