from .common import *

@login_required
def OrderHistoryView(request):
    order_num = request.POST.get('order_num')
    order_status = request.POST.get('order_status')
    date = request.POST.get('date')
    orderHistorySql ="SELECT a.buy_date, a.order_num, a.order_name, c.book_name, " \
                     "sum(b.quantity), sum(b.purchased_price), b.order_status FROM order_info as a " \
                     "JOIN order_products as b ON a.order_num = b.order_num " \
                     "JOIN book AS c ON b.isbn = c.isbn WHERE " \
                     "a.order_num like '%" + order_num + "%' " \
                     "and b.order_status like '%" + order_status + "%' " \
                     "and date(a.buy_date) like '%" + date + "%' " \
                     "group by a.order_num order by buy_date desc"

    datas = execute_and_get(orderHistorySql)

    order_history = []
    for data in datas:
        row = {'buy_date': data[0],
               'order_num': data[1],
               'order_name': data[2],
               'book_name': data[3],
               'book_count': data[4],
               'sum_price': data[5],
               'order_status':data[6],
               }
        order_history.append(row)

    return render(request, 'mypage.html', {'order_history': order_history, 'order_num': order_num})