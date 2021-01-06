from .common import *

@login_required
def ReviewManageView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))

    lately_review_sql = "SELECT user_id, title, content, evaluate_score, id, date, book_name, answer " \
                        "FROM review WHERE store_id= (%s) ORDER BY date DESC"
    datas = execute_and_get(lately_review_sql, (store_id[0][0],))
    lately_review = []
    for data in datas:
        row = {'user_id': data[0],
               'title': data[1],
               'content': data[2],
               'evaluate_score': data[3],
               'id': data[4],
               'date': data[5],
               'book_name': data[6],
               'answer': data[7],
               }
        lately_review.append(row)

    avg_sql = "SELECT round(avg(evaluate_score),2), round(avg(evaluate_score)) FROM review WHERE store_id = (%s)"
    data = execute_and_get(avg_sql, (store_id[0][0],))
    avg = {'avg': data[0][0],
           'star': data[0][1],
           }

    best_sql = "SELECT book.book_name, round(avg(evaluate_score),2) as avg, book_img " \
               "FROM review join book on review.book_isbn = book.isbn " \
               "WHERE store_id= (%s) group by book_isbn order by avg desc limit 3"

    datas = execute_and_get(best_sql, (store_id[0][0],))
    best = []
    best_rank = 0
    for data in datas:
        best_rank += 1
        row = {'book_name': data[0],
               'avg': data[1],
               'book_img': data[2],
               'rank': best_rank,
               }
        best.append(row)

    worst_sql = "SELECT book.book_name, round(avg(evaluate_score),2) as avg, book_img " \
                "FROM review join book on review.book_isbn = book.isbn " \
                "WHERE store_id= (%s) group by book_isbn order by avg limit 3"

    datas = execute_and_get(worst_sql, (store_id[0][0],))
    worst = []
    worst_rank = 0
    for data in datas:
        worst_rank += 1
        row = {'book_name': data[0],
               'avg': data[1],
               'book_img': data[2],
               'rank': worst_rank,
               }
        worst.append(row)

    return render(request, 'review_manage.html', {'lately_review': lately_review, 'avg':avg, 'best': best, 'worst': worst})