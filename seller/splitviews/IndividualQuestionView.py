from .common import *

@login_required
def IndividualQuestionView(request, store_id):
    user = request.user

    unanswered_question_counts = execute_and_get("SELECT COUNT(*) FROM individual_question WHERE store_id = (%s) AND answer_complete = (%s)",
                            (store_id, 0,))

    answered_question_counts = execute_and_get("SELECT COUNT(*) FROM individual_question WHERE store_id = (%s) AND answer_complete = (%s)",
                            (store_id, 1,))

    question_count = {
        'unanswered_question_counts': unanswered_question_counts[0][0],
        'answered_question_counts': answered_question_counts[0][0],
    }

    question_datas = execute_and_get("SELECT customer_id, title, content, answer, time, answer_complete, id FROM individual_question " +
                                     "WHERE store_id = (%s)", (store_id,))

    question_info = []
    for data in question_datas:
        row = {
            'customer_id': data[0],
            'title': data[1],
            'content': data[2],
            'answer': data[3],
            'time': data[4],
            'answer_complete': data[5],
            'id': data[6]
        }
        question_info.append(row)

    return render(request, 'seller_individual_question.html', {'question_count': question_count, 'question_info': question_info})
