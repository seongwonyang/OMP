from .common import *

@login_required
def SettlementCheckView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))
    if request.method == 'GET':
        product_sql = "SELECT a.order_num, b.purchased_price, a.buy_date, settlement " \
                      "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                      "WHERE b.store_id = (%s) and b.order_status = (%s) " \
                      "order by a.buy_date desc"
        datas = execute_and_get(product_sql, (store_id[0][0], '구매 확정',))
        settlement_info = []
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],
                   'buy_date': data[2],
                   'settlement_status': data[3], }
            settlement_info.append(row)
        return render(request, 'settlement_check.html', {'settlement_info': settlement_info})

    else:
        settlement_status = request.POST.get('settlement_status')

        product_sql = "SELECT a.order_num, b.purchased_price, a.buy_date, settlement " \
                      "FROM order_info as a JOIN order_products as b on a.order_num = b.order_num " \
                      "WHERE b.store_id = (%s) and b.order_status = (%s) and b.settlement like '%%" + settlement_status + "%%' " \
                      "order by a.buy_date desc"

        datas = execute_and_get(product_sql, (store_id[0][0], '구매 확정',))
        settlement_info = []
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],
                   'buy_date': data[2],
                   'settlement_status': data[3], }
            settlement_info.append(row)
        return render(request, 'settlement_check.html', {'settlement_info': settlement_info})