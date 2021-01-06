from .common import *

@login_required
def FrequentQuestionView(request):
    user = request.user
    store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    if request.method == "GET":
        question_datas = execute_and_get("SELECT title, content, id FROM frequent_question WHERE store_id = (%s)", (store_id[0][0],))

        question_info = []
        for data in question_datas:
            row = {
                'title': data[0],
                'content': data[1],
                'id': data[2],
            }
            question_info.append(row)

        unanswered_question_count = execute_and_get("SELECT COUNT(*) FROM individual_question WHERE store_id = (%s) AND answer_complete = (%s)",
                                                     (store_id[0][0], 0,))

        return render(request, ('frequent_question.html'), {'question_info': question_info, 'unanswered_question_count': unanswered_question_count[0][0],
                                                            'store_id': store_id[0][0]})

    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        execute("INSERT INTO frequent_question(store_id, title, content) " +
                "VALUES ((%s), (%s), (%s))", (store_id[0][0], title, content))

        return redirect('seller:frequent_question')