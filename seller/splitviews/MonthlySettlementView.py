from .common import *
from datetime import datetime

@login_required
def MonthlySettlementView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))
    if request.method == 'GET':
        current_date = datetime.today().strftime('%Y-%m')
        bank_sql = "SELECT a.order_num, a.purchased_price " \
                   "FROM order_products as a JOIN order_info as b ON a.order_num = b.order_num " \
                   "WHERE a.store_id = (%s) and a.settlement = '정산 완료' " \
                   "and b.payment = 'bank' and a.delivery_compl_time like '%%" + current_date + "%%' "
        datas = execute_and_get(bank_sql,(store_id[0][0],))
        bank = []
        bank_sum = 0
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],}
            bank.append(row)
            bank_sum += int(data[1])

        card_sql = "SELECT a.order_num, a.purchased_price " \
                   "FROM order_products as a JOIN order_info as b ON a.order_num = b.order_num " \
                   "WHERE a.store_id = (%s) and a.settlement = '정산 완료' " \
                   "and b.payment = 'card' and a.delivery_compl_time like '%%" + current_date + "%%' " 
        datas = execute_and_get(card_sql,(store_id[0][0],))
        card = []
        card_sum = 0
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1],}
            card.append(row)
            card_sum += int(data[1])

        sum = int(bank_sum + card_sum)
        commission = int(sum*0.1)
        result = int(sum - commission)
        return render(request, 'monthly_settlement.html', {'bank': bank, 'card': card, 'bank_sum': bank_sum, 'card_sum': card_sum,
                                                           'sum':sum, 'commission':commission, 'result':result})

    else:
        date = request.POST.get('date')
        bank_sql = "SELECT a.order_num, a.purchased_price " \
                   "FROM order_products as a JOIN order_info as b ON a.order_num = b.order_num " \
                   "WHERE a.store_id = (%s) and a.settlement = '정산 완료' " \
                   "and b.payment = 'bank' and a.delivery_compl_time like '%%" + date + "%%' "
        datas = execute_and_get(bank_sql, (store_id[0][0],))
        bank = []
        bank_sum = 0
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1], }
            bank.append(row)
            bank_sum += int(data[1])

        card_sql = "SELECT a.order_num, a.purchased_price " \
                   "FROM order_products as a JOIN order_info as b ON a.order_num = b.order_num " \
                   "WHERE a.store_id = (%s) and a.settlement = '정산 완료' " \
                   "and b.payment = 'card' and a.delivery_compl_time like '%%" + date + "%%' "
        datas = execute_and_get(card_sql, (store_id[0][0],))
        card = []
        card_sum = 0
        for data in datas:
            row = {'order_num': data[0],
                   'purchased_price': data[1], }
            card.append(row)
            card_sum += int(data[1])

        sum = int(bank_sum + card_sum)
        commission = int(sum*0.1)
        result = int(sum - commission)
        return render(request, 'monthly_settlement.html', {'bank': bank, 'card': card, 'bank_sum': bank_sum, 'card_sum': card_sum,
                                                           'sum':sum, 'commission':commission, 'result':result})