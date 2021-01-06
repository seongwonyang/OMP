from .common import *

def LoginView(request):
    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")

        login_user = authenticate(request, username=user_id, password=user_pw)

        if login_user is not None and login_user.user_type == 2:
            login(request, login_user)
            return redirect('customer:main')

        elif login_user is not None and login_user.user_type == 3:
            login(request, login_user)

            sellerIdSql = "SELECT EXISTS (SELECT seller_id FROM bookstore WHERE seller_id = (%s))"
            seller_id_data = execute_and_get(sellerIdSql, (user_id,))
            is_seller_id = seller_id_data[0][0]
            if is_seller_id == True:
                return redirect('seller:main')
            else:
                return redirect('seller_accounts:bookstore_register')

        else:
            messages.error(request,'ID 또는 비밀번호 오류입니다.')
            return redirect('customer_accounts:login')
