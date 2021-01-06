from .common import *
from datetime import datetime

@login_required

def OrderCreateView (request):

    if request.method == 'POST':

        name = request.POST.get("name")
        address = request.POST.get("address")
        p_num = request.POST.get("p_number")
        e_mail = request.POST.get("e_mail")
        memo = request.POST.get("memo")
        payment = request.POST.get("payment")

        user_id = request.user

        idIntSql = "SELECT id FROM customer_accounts_user WHERE username = (%s)"
        id_int = execute_and_get(idIntSql,(user_id,))

        order_num = str(id_int[0][0]) +str(int(datetime.today().strftime("%Y%m%d%H%M%S")) + random.randrange(10000,99999))

        orderSql = "INSERT INTO order_info(user_id, order_name, " \
                   "order_address, order_p_num, order_email, order_memo, payment, order_num) " \
                   "VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
        execute(orderSql, (user_id, name, address, p_num, e_mail, memo, payment, order_num,))

        if len(order_num) != 0:
            store = request.POST.getlist("store")
            book = request.POST.getlist("book")
            price = request.POST.getlist("price")
            quantity = request.POST.getlist('quantity')

            if len(store) >= 2:
                for i in range(len(store)):
                    storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
                    store_id = execute_and_get(storeIdSql, (store[i],))

                    isbnSql = "SELECT book_isbn FROM book_inven " \
                              "where book_name = (%s) and store_id = (%s)"
                    isbn = execute_and_get(isbnSql, (book[i], store_id,))

                    if payment in "bank":
                        listSql = "INSERT INTO order_products(order_num, store_id, isbn, purchased_price, order_status, quantity) " \
                                  "VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
                        execute(listSql, (order_num, store_id, isbn, int(price[i])*int(quantity[i]), '결제 대기중',quantity[i],))

                    elif payment in "card":
                        listSql = "INSERT INTO order_products(order_num, store_id, isbn, purchased_price, order_status, quantity) " \
                                  "VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
                        execute(listSql,(order_num, store_id, isbn, int(price[i])*int(quantity[i]), '결제 완료', quantity[i],))
                        inven_sql = "UPDATE book_inven SET inven = inven-(%s) WHERE book_isbn = (%s) and store_id = (%s)"
                        execute(inven_sql, (int(quantity[i]), isbn, store_id,))

                    execute("UPDATE book_inven SET inven = inven-(%s) WHERE book_name = (%s) AND store_id = (%s)",
                            (quantity[i], book[i], store_id))

            else:
                storeIdSql = "SELECT id FROM bookstore where store_name=(%s)"
                store_id = execute_and_get(storeIdSql, (store,))

                isbnSql = "SELECT book_isbn FROM book_inven " \
                          "where book_name = (%s) and store_id = (%s)"
                isbn = execute_and_get(isbnSql, (book, store_id,))

                if payment in "bank":
                    listSql = "INSERT INTO order_products(order_num, store_id, isbn, purchased_price, order_status, quantity) " \
                              "VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
                    execute(listSql, (order_num, store_id, isbn, int(price[0])*int(quantity[0]), '결제 대기중', quantity,))

                elif payment in "card":
                    listSql = "INSERT INTO order_products(order_num, store_id, isbn, purchased_price, order_status, quantity) " \
                              "VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
                    execute(listSql, (order_num, store_id, isbn, int(price[0])*int(quantity[0]), '결제 완료', quantity,))
                    inven_sql = "UPDATE book_inven SET inven = inven-(%s) WHERE book_isbn = (%s) and store_id = (%s)"
                    execute(inven_sql, (int(quantity[0]), isbn, store_id,))

                execute("UPDATE book_inven SET inven = inven-(%s) WHERE book_name = (%s) AND store_id = (%s)",
                        (quantity, book, store_id))

            return redirect('customer:order_confirm', order_num = order_num)