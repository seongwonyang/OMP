from .common import *

@login_required
def AjaxGetReviewAnswerView(request, review_id):

    answer_sql = "SELECT answer FROM review WHERE id=(%s)"
    data = execute_and_get(answer_sql, (review_id,))

    answer_info = {'answer': data[0][0],
                   'id': review_id,}

    return HttpResponse(json.dumps({'answer_info': answer_info}), content_type="application/json")