from .common import *

@csrf_exempt
@login_required
def ReviewAnswerView(request):
    answer = request.POST.get('answer')
    review_id = request.POST.get('review_id')

    answer_sql = "UPDATE review SET answer = (%s) WHERE id = (%s)"
    execute(answer_sql, (answer, review_id,))

    return redirect('seller:review_manage')