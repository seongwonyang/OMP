from .common import *

@login_required
def IndividualQuestionAnswerView(request, question_id):
    user = request.user
    store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    answer = request.POST.get("modal_answer")

    execute("UPDATE individual_question SET answer=(%s), answer_complete=1 WHERE id = (%s)", (answer, question_id))

    return redirect('seller:individual_question', store_id[0][0])