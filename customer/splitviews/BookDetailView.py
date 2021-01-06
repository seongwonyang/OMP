from .common import *

def BookDetailView(request, book_isbn, store_id):
    user = request.user
    book_datas = execute_and_get("SELECT book_name, author,  publisher, book_img, isbn" +
                                " FROM book WHERE isbn = (%s)", (book_isbn,))

    current_book_store_name = execute_and_get("SELECT store_name, bookstore.id FROM bookstore" +
                                      " LEFT OUTER JOIN book_inven on book_inven.store_id = bookstore.id WHERE book_inven.book_isbn = (%s) AND store_id = (%s)", (book_isbn, store_id,))

    is_like = execute_and_get("SELECT exists (SELECT * FROM like_list WHERE user_id = (%s) AND book_isbn = (%s) AND store_id = (%s))",
                              (user.username, book_isbn, store_id,))

    book_inven = execute_and_get("SELECT inven, price, book_msg, detail_img FROM book_inven  WHERE book_name = (%s) AND store_id= (%s)",
                                 (book_datas[0][0], store_id,))

    book_review_datas = execute_and_get("SELECT ROUND(AVG(evaluate_score),1), COUNT(book_name), user_id, title, content, evaluate_score" +
                                   " FROM review WHERE book_name= (%s) AND store_id = (%s)",
                                   (book_datas[0][0], store_id,))

    review_list = execute_and_get("SELECT user_id, title, content, evaluate_score, id, answer FROM review WHERE book_name= (%s) AND store_id= (%s) ORDER BY CAST(evaluate_score AS signed integer) DESC",
                        (book_datas[0][0], store_id,))

    book = {'book_name': book_datas[0][0],
            'author': book_datas[0][1],
            'publisher': book_datas[0][2],
            'price': book_inven[0][1],
            'book_msg': book_inven[0][2],
            'book_img': book_datas[0][3],
            'isbn': book_datas[0][4],
            'store_name': current_book_store_name[0][0],
            'store_id': current_book_store_name[0][1],
            'book_inven': book_inven[0][0],
            'review_score': book_review_datas[0][0],
            'review_count': book_review_datas[0][1],
            'detail_img': book_inven[0][3]
            }

    review = []
    for review_data in review_list:
        review_row = {
            'user_id': review_data[0],
            'title': review_data[1],
            'content': review_data[2],
            'evaluate_score': review_data[3],
            'id': review_data[4],
            'answer': review_data[5],
        }
        review.append(review_row)

    return render(request, "book_detail.html", {'book': book, 'is_like': is_like[0][0], 'review': review, 'book_isbn':book_isbn, 'store_id':store_id,})

