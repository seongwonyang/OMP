from .common import *

@login_required
def ProductRegisterView(request):
    if request.method == 'GET':
        return render(request, 'product_register.html')

    elif request.method == 'POST':
        user = request.user

        book_name = request.POST.get('book_name')
        book_isbn = request.POST.get('book_isbn')
        inven = request.POST.get('inven')
        price = request.POST.get('price')
        book_img = request.FILES.get('book_img')
        book_msg = request.POST.get('book_msg')

        book_img_url = None
        if book_img != None:
            book_img_url = fileUpload(user, book_img)

        store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

        execute("INSERT INTO book_inven(book_isbn, book_name, store_id, inven, price, detail_img, book_msg) "+
                "VALUES ((%s), (%s), (%s), (%s), (%s), (%s), (%s))", (book_isbn, book_name, store_id[0][0], inven, price, book_img_url, book_msg))

        return redirect('seller:main')




