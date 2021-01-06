from .common import *

def RegisterView(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        name = request.POST.get("name")
        user_id = request.POST.get("user_id")
        user_pw = request.POST.get("user_pw")
        user_2nd_pw = request.POST.get("user_2nd_pw")
        e_mail = request.POST.get("e_mail")
        phone_number = request.POST.get("p_number")
        address = request.POST.get("address")

        try:
            user = User.objects.get(username=user_id)
            messages.error(request, "이미 존재하는 계정입니다.")
            return redirect('customer_accounts:register')

        except ObjectDoesNotExist:
            if user_pw == user_2nd_pw:
                new_user = User.objects.create_user(first_name=name, username=user_id, password=user_pw,
                                                    email=e_mail, phone_number=phone_number, address=address)
                new_user.save()

                messages.success(request, "회원가입에 성공하였습니다.")
                return redirect('customer_accounts:login')

            else:
                messages.error(request, "비밀번호가 일치하지 않습니다.")
                return redirect('customer_accounts:register')