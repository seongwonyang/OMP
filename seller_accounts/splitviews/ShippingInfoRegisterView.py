from .common import *

@login_required

def ShippingInfoRegisterView(request):
    if request.method == "GET":
        return render(request, 'shipping_info_registration.html')

    elif request.method == "POST":
        user = request.user
        idSql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
        store_id = execute_and_get(idSql, (user,))

        bank = request.POST.get("bank")
        account = request.POST.get("bank_account")
        shipping_policy = request.POST.get("shipping_policy")
        send_address = request.POST.get("send_address")
        return_address = request.POST.get("return_address")

        info_insert_sql = "INSERT INTO shipping_info(bookstore_id, bank, account, " \
                          "shipping_policy, send_address, return_address )" \
                          "VALUES ((%s),(%s),(%s),(%s),(%s),(%s))"
        execute(info_insert_sql, (store_id[0][0], bank, account, shipping_policy, send_address, return_address,))
        messages.success(request, "배송 정보 등록에 성공하였습니다.")
        return redirect('seller:main')