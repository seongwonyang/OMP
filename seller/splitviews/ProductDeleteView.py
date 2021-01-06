from .common import *

@login_required
def ProductDeleteView(request, store_id, isbn):

    execute("DELETE FROM book_inven WHERE book_isbn = (%s) AND store_id = (%s)", (isbn, store_id,))

    return redirect('seller:product_list')