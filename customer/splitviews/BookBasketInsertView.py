from .common import *

@login_required
def BookBasketInsertView(request, book_isbn, store_id):
    if 'user_basket' not in request.session:
        request.session['user_basket'] = []

    tab = 'basket'
    quantity = request.POST.get('quantity')

    book_info = execute_and_get("SELECT book_name, book_img, publisher, isbn FROM book WHERE isbn = (%s)", (book_isbn,))
    store_name = execute_and_get("SELECT store_name FROM bookstore WHERE id = (%s)", (store_id,))
    price = execute_and_get("SELECT price FROM book_inven WHERE book_isbn = (%s) AND store_id = (%s)", (book_isbn, store_id,))

    for i in range(len(request.session['user_basket'])):
        if request.session['user_basket'][i]['isbn'] == book_isbn and request.session['user_basket'][i]['store_id'] == store_id:
            messages.error(request ,'이미 해당 서점의 도서가 장바구니에 존재합니다.')
            return redirect('customer:book_detail', book_isbn, store_id)

    book = {'book_name': book_info[0][0],
            'book_img': book_info[0][1],
            'price': price[0][0]*int(quantity),
            'publisher': book_info[0][2],
            'isbn':book_info[0][3],
            'store_name': store_name[0][0],
            'store_id': store_id,
            'quantity':quantity,}

    request.session['user_basket'].append(book)
    request.session.modified = True

    return render(request, 'mypage.html', {'tab': tab})