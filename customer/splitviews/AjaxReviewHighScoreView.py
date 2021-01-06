from .common import *

def AjaxReviewHighScoreView(request, book_isbn):
    user = request.user
    review_data = execute_and_get('SELECT user_id, title, content, evaluate_score, id FROM review WHERE book_isbn= (%s) ORDER BY convert(evaluate_score, signed integer) DESC',
                                    (book_isbn,))

    review = []
    for review_datas in review_data:
        review_row = {
            'user_id': review_datas[0],
            'title': review_datas[1],
            'content': review_datas[2],
            'evaluate_score': review_datas[3],
            'id': review_datas[4],
            'login_user': user.username,
        }
        review.append(review_row)

    return HttpResponse(json.dumps({'review': review}), content_type='application/json')