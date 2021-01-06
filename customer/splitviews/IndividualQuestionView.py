from .common import *

@login_required
def IndividualQuestionView(request, store_id):
    user = request.user

    if request.method == "GET":
        store_name = execute_and_get("SELECT store_name FROM bookstore WHERE id = (%s)", (store_id,))

        question_datas = execute_and_get("SELECT title, content, answer, time, answer_complete FROM individual_question " +
                                         "WHERE store_id = (%s) AND customer_id = (%s) ORDER BY time DESC", (store_id, user.username,))

        question_info = []
        for data in question_datas:
            row = {
                'title': data[0],
                'content': data[1],
                'answer': data[2],
                'time': data[3],
                'answer_complete': data[4],
            }
            question_info.append(row)


        return render(request, 'individual_question.html', {'store_name': store_name[0][0], 'store_id': store_id,
                                                            'question_info': question_info})

    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        execute("INSERT INTO individual_question(store_id, customer_id, title, content) " +
                "VALUES((%s), (%s), (%s), (%s))", (store_id, user.username, title, content,))

        return redirect('customer:individual_question', store_id)