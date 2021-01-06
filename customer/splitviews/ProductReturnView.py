from .common import *

@login_required
def ProductReturnView(request, order_id):
    if request.method == "GET":
        product_info = execute_and_get("SELECT store_id , isbn, purchased_price FROM order_products WHERE id = (%s)", (order_id,))

        book_name = execute_and_get("SELECT book_name FROM book WHERE isbn = (%s)", (product_info[0][1],))
        store_name = execute_and_get("SELECT store_name FROM bookstore WHERE id = (%s)", (product_info[0][0],))

        order_info = {'book_name': book_name[0][0],
                      'price': product_info[0][2],
                      'bookstore': store_name[0][0]}

        return render(request, 'product_return.html', {'order_id': order_id, 'order_info': order_info})

    elif request.method == "POST":
        user = request.user

        user_id = user.username
        order_product_id = order_id
        return_reason = request.POST.get('return_msg')
        product_img = request.FILES.get('product_img')

        if return_reason == "직접입력":
            return_reason = request.POST.get('direct_msg')

        product_img_url = None
        if product_img != None:
            product_img_url = fileUpload(user, product_img)

        execute("INSERT INTO product_return(user_id, order_product_id, return_reason, product_img)"+
                " VALUES ((%s), (%s), (%s), (%s))", (user.username, order_id, return_reason, product_img_url,))

        execute("UPDATE order_products SET order_status = '반품 접수중' WHERE id = (%s)", (order_id,))

        return redirect('customer:mypage')