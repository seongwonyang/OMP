from .common import *

@login_required
def SellerDeleteView(request):
    user = request.user

    tab_is = 2

    if request.method == "POST":
        user_id = request.POST.get('id')
        user_password = request.POST.get('password')

        if user.username == user_id and user.check_password(user_password):
            store_delete_sql = "DELETE FROM bookstore WHERE seller_id =(%s)"
            execute(store_delete_sql, (user_id,))

            inven_delete_sql = "DELETE a FROM book_inven AS a " \
                               "LEFT JOIN bookstore AS b ON a.store_id = b.id where seller_id = (%s)"
            execute(inven_delete_sql, (user_id,))

            likebook_delete_sql = "DELETE a FROM like_list AS a " \
                                  "LEFT JOIN bookstore AS b ON a.store_id = b.id where seller_id = (%s)"
            execute(likebook_delete_sql, (user_id,))

            favoritestore_delete_sql = "DELETE a FROM favorite_bookstore AS a " \
                                       "LEFT JOIN bookstore AS b ON a.store_id = b.id where seller_id = (%s)"
            execute(favoritestore_delete_sql, (user_id,))

            review_delete_sql = "DELETE a FROM review AS a " \
                                "LEFT JOIN bookstore AS b ON a.store_id = b.id where seller_id = (%s)"
            execute(review_delete_sql, (user_id,))

            user.delete()
            messages.success(request,'회원탈퇴가 정상적으로 완료되었습니다.')
            return redirect('customer_accounts:login')
        else:
            messages.error(request, '입력하신 정보가 정확하지 않습니다.')
            return render(request, 'info_manage.html', {'tab_is': tab_is})

