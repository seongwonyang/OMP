from .common import *

@login_required

def ShippingInfoModifyView(request):
    if request.method == "POST":
        user = request.user
        idSql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
        store_id = execute_and_get(idSql, (user,))

        bank = request.POST.get("bank")
        account = request.POST.get("bank_account")
        shipping_policy = request.POST.get("shipping_policy")
        send_address = request.POST.get("send_address")
        return_address = request.POST.get("return_address")

        updateSql = "UPDATE shipping_info SET bank = (%s), account = (%s), shipping_policy = (%s), " \
                    "send_address = (%s), return_address = (%s) " \
                    "WHERE bookstore_id = (%s)"
        execute(updateSql, (bank, account, shipping_policy, send_address, return_address, store_id[0][0],))

        return redirect('seller_accounts:seller_info')