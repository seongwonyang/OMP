from .common import *

@login_required
def BookBasketDeleteView(request, book_isbn):
    tab = 'basket'

    for i in range(len(request.session['user_basket'])):
        if request.session['user_basket'][i]['isbn'] == book_isbn:
            del request.session['user_basket'][i]
            break

    request.session.modified = True

    return render(request, 'mypage.html', {'tab': tab})