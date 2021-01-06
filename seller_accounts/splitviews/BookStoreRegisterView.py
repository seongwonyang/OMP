from .common import *

@login_required

def BookStoreRegisterView(request):
    if request.method == "GET":
        return render(request, 'bookstore_registration.html')

    elif request.method == "POST":
        user = request.user

        business_num = request.POST.get("business_num")
        store_name = request.POST.get("store_name")
        repre_name = request.POST.get("repre_name")

        address = request.POST.get("address")
        store_number = request.POST.get("store_number")
        store_email = request.POST.get("e_mail")
        store_msg = request.POST.get("store_msg")

        store_img = request.FILES.get('store_img')

        store_img_url = fileUpload(user, store_img)

        businessNumSql = "SELECT exists (SELECT business_num from bookstore where business_num = (%s))"
        is_businessNum = execute_and_get(businessNumSql,(business_num,))

        if is_businessNum[0][0] == False:

            orderSql = "INSERT INTO bookstore(store_name, repre_name, " \
                       "address, store_num, store_email, store_msg, bookstore_img, seller_id, business_num) " \
                       "VALUES ((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))"
            execute(orderSql, (store_name, repre_name, address, store_number, store_email, store_msg, store_img_url, user, business_num,))
            messages.success(request, "서점 정보 등록에 성공하였습니다. 배송정보를 입력해주세요.")
            return redirect('seller_account:shipping_info_register')

        else:
            messages.error(request, "이미 등록된 사업자번호입니다.")
            return redirect('seller_accounts:bookstore_register')