from .common import *

@login_required
def ProductModifyView(request):
    store_id = request.POST.get('store_id')
    isbn = request.POST.get('isbn')
    inven = request.POST.get('inven')
    price = request.POST.get('price')
    book_msg = request.POST.get('book_msg')

    update_sql = "UPDATE book_inven SET inven = (%s), price = (%s), book_msg = (%s) " \
                 "WHERE store_id = (%s) and book_isbn = (%s) "
    execute(update_sql, (inven, price, book_msg, store_id, isbn,))

    return redirect('seller:product_list')