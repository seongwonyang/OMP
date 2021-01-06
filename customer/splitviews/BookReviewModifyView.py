from .common import *

@login_required
def BookReviewModifyView(request, review_id):
    user = request.user

    current_review = execute_and_get('SELECT title, content FROM review WHERE user_id = (%s) AND id = (%s)',
                                     (user.username, review_id,))

    isbn_and_storeId = execute_and_get("SELECT book_isbn, store_id FROM review WHERE id = (%s)", (review_id,))

    if request.method == "GET":
        current_review_data = {
            'title': current_review[0][0],
            'content': current_review[0][1],
            'review_id': review_id
        }

        return HttpResponse(json.dumps({'current_review_data': current_review_data}), content_type="application/json")

    elif request.method == "POST":
        title = request.POST.get("modal_review_title")
        evaluate_score = request.POST.get("modal_review_evaluate_score")
        content = request.POST.get("modal_review_content")

        execute("UPDATE review SET title = (%s), content = (%s), evaluate_score = (%s) WHERE id = (%s)",
                (title, content, evaluate_score, review_id,))

        return redirect('customer:book_detail', isbn_and_storeId[0][0], isbn_and_storeId[0][1])