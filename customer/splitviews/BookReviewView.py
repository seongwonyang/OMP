from .common import *

@login_required
def BookReviewView(request, book_isbn, store_id):
    user = request.user

    title = request.POST.get('title')
    evaluate_score = request.POST.get('evaluate_score')
    content = request.POST.get('content')

    book_name = execute_and_get('SELECT book_name FROM book WHERE isbn = (%s)',
                                (book_isbn,))


    review = execute("INSERT INTO review(user_id, book_isbn, book_name, title, content, evaluate_score, store_id)"
    +"VALUES ((%s), (%s), (%s), (%s), (%s), (%s), (%s))",
                             (user.username, book_isbn, book_name[0][0], title, content, evaluate_score, store_id,))

    return redirect('customer:book_detail', book_isbn, store_id)