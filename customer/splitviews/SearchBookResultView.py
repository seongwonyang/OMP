from .common import *

def SearchBookResultView(request):
    cursor = connection.cursor()

    title = request.GET.get('title')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')

    search_keyword = {'title': title,
                      'author': author,
                      'publisher': publisher,}

    search_datas = execute_and_get("SELECT book_name, author, publisher, book_img, isbn FROM book" +
                             " WHERE book_name LIKE '%" + title + "%' AND author LIKE '%" + author + "%' AND publisher LIKE '%" + publisher + "%' GROUP BY book_name")

    search_list = []
    for search_data in search_datas:
        store_data = execute_and_get("SELECT store_id, inven, store_name FROM book_inven "+
                                     "LEFT OUTER JOIN bookstore on bookstore.id = book_inven.store_id WHERE book_isbn = (%s)", (search_data[4],))

        for i in range(len(store_data)):
            review_score = execute_and_get("SELECT ROUND(AVG(evaluate_score),1), COUNT(*) FROM review WHERE book_isbn = (%s) AND store_id = (%s)", (search_data[4], store_data[i][0],))

            price_sql = execute_and_get("SELECT price FROM book_inven WHERE book_isbn = (%s) AND store_id = (%s)",
                                        (search_data[4], store_data[i][0],))

            row = {'book_name': search_data[0],
                   'author': search_data[1],
                   'publisher': search_data[2],
                   'book_img': search_data[3],
                   'price': price_sql[0][0],
                   'book_isbn': search_data[4],
                   'store_id': store_data[i][0],
                   'inven': store_data[i][1],
                   'store_name': store_data[i][2],
                   'review_score': review_score[0][0],
                   'review_count': review_score[0][1],
                }
            search_list.append(row)

    connection.commit()
    connection.close()

    result = 1  # 검색결과가 있을 때와 없을 때 구분
    if len(search_list) == 0:
        result = 0

    # 검색키워드가 아무것도 입력되지 않았을 때
    if title == "" and author == "" and publisher == "":
        messages.error(request, '검색 키워드를 하나 이상 입력해주세요.')
        return redirect('customer:search_book')

    return render(request, 'search_book_result.html', {'search_list': search_list, 'search_keyword': search_keyword,
                                                       'result': result})
