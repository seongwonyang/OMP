from .common import *

@login_required
def customerInfoModify(request):
    user = request.user

    if request.method == "GET":
        return render(request, 'customer_info_modify.html')

    elif request.method == "POST":
        name = request.POST.get('name')
        user_id = request.POST.get('user_id')
        e_mail = request.POST.get('e_mail')
        phone_number = request.POST.get('p_number')
        address = request.POST.get('address')

        user.first_name = name
        user.username = user_id
        user.email = e_mail
        user.phone_number = phone_number
        user.address = address

        user.save()

        return redirect('accounts:customerInfoModify')