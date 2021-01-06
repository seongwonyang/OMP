from .common import *

def FrequentQuestionView(request, store_id):
    user = request.user

    datas = execute_and_get("SELECT title, content, id FROM frequent_question WHERE store_id = (%s)", (store_id,))

    question_info = []
    for data in datas:
        row = {
            'title': data[0],
            'content': data[1],
            'id': data[2],
        }
        question_info.append(row)

    return render(request, 'frequently_question.html', {'question_info': question_info, 'store_id': store_id})