from .common import *

@login_required
def DeliveryCheckView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))
    if request.method == 'GET':
        product_sql = "SELECT a.order_num, b.purchased_price, b.order_status, a.buy_date " \
                     "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                     "WHERE b.store_id = (%s) and b.order_status in ((%s), (%s), (%s)) " \
                     "order by a.buy_date desc"
        delivery_datas = execute_and_get(product_sql, (store_id[0][0], '결제 완료', '배송 준비', '배송 중',))
        delivery_info = []
        for data in delivery_datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],
                   'order_status': data[2],
                   'buy_date': data[3], }
            delivery_info.append(row)
        return render(request, 'delivery_check.html', {'delivery_info': delivery_info})

    else:
        order_status = request.POST.get('order_status')
        product_sql ="SELECT a.order_num, b.purchased_price, b.order_status, a.buy_date " \
                     "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                     "WHERE b.store_id = (%s) and b.order_status in ((%s), (%s), (%s)) " \
                     "and b.order_status like '%%" + order_status + "%%' " \
                     "order by a.buy_date desc"
        delivery_datas = execute_and_get(product_sql,(store_id[0][0],'결제 완료','배송 준비','배송 중',))
        delivery_info = []
        for data in delivery_datas:
            row = {'order_num':data[0],
                   'purchased_price': data[1],
                   'order_status': data[2],
                   'buy_date': data[3],}
            delivery_info.append(row)
        return render(request, 'delivery_check.html', {'delivery_info': delivery_info})