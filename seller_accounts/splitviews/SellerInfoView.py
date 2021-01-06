from .common import *

@login_required
def SellerInfoView(request):
    tab_is = 0
    user = request.user
    store_sql = "SELECT store_name, address, store_num, bookstore_img, store_msg, store_email, repre_name " \
                "FROM bookstore WHERE seller_id = (%s)"
    store_data = execute_and_get(store_sql, (user,))

    if len(store_data) == 0 :
        messages.success(request, "마이페이지는 서점 등록 후 이용가능합니다.")
        return redirect('seller_accounts:bookstore_register')

    else:
        info_sql = "SELECT bookstore_id, bank, account, shipping_policy, send_address, return_address " \
                   "FROM shipping_info as a " \
                   "JOIN bookstore as b " \
                   "ON a.bookstore_id = b.id " \
                   "WHERE b.seller_id = (%s)"
        info_data = execute_and_get(info_sql, (user,))

        if len(info_data) == 0:
            messages.success(request, "마이페이지는 배송 정보 등록 후 이용가능합니다.")
            return redirect('seller_accounts:shipping_info_register')

        else:
            store = {'store_name': store_data[0][0],
                     'address': store_data[0][1],
                     'store_num': store_data[0][2],
                     'store_img': store_data[0][3],
                     'store_msg': store_data[0][4],
                     'store_email': store_data[0][5],
                     'repre_name': store_data[0][6],
                     }

            shipping_info = {'store_id': info_data[0][0],
                             'bank': info_data[0][1],
                             'account': info_data[0][2],
                             'shipping_policy': info_data[0][3],
                             'send_address': info_data[0][4],
                             'return_address': info_data[0][5],
                             }

            return render(request, 'seller_info.html', {'store':store, 'shipping_info': shipping_info, 'tab_is': tab_is})