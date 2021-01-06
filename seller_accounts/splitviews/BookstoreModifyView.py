from .common import *

@login_required
def BookstoreModifyView(request, user_id):
    user = request.user

    if request.method == "POST":
        store_name = request.POST.get('store_name')
        repre_name = request.POST.get('repre_name')
        address = request.POST.get('address')
        store_number = request.POST.get('store_number')
        e_mail = request.POST.get('e_mail')
        store_img = request.FILES.get('store_img')

        store_img_url = fileUpload(user, store_img)
        store_msg = request.POST.get('store_msg')

        updateSql = "UPDATE bookstore SET store_name = (%s), repre_name = (%s), address = (%s), store_msg = (%s), " \
                    "store_num = (%s), store_email = (%s), bookstore_img = (%s) " \
                    "WHERE seller_id = (%s)"
        execute(updateSql, (store_name, repre_name, address, store_msg, store_number, e_mail, store_img_url, user,))

        return redirect('seller_accounts:seller_info')