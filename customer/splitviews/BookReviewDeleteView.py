from .common import *

@login_required
def BookReviewDeleteView(request, review_id):
    user = request.user

    review_data = execute_and_get("SELECT book_isbn, store_id FROM review WHERE id = (%s)", (review_id,))

    execute("DELETE FROM review WHERE user_id = (%s) AND id = (%s)", (user.username, review_id,))

    return redirect('customer:book_detail', review_data[0][0], review_data[0][1])