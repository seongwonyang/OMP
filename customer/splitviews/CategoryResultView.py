from .common import *

def CategoryResultView (request,main_category_id):

    mainSql = "SELECT main_category FROM main_category where id=(%s)"

    data = execute_and_get(mainSql, (main_category_id,))
    main = data[0][0]

    bookSql = "SELECT distinct a.isbn, a.book_name, a.book_img, a.publisher, a.author " \
              "FROM book AS a " \
              "JOIN book_inven AS b " \
              "ON a.isbn = b.book_isbn " \
              "where category_id = (%s)"

    datas = execute_and_get(bookSql,(main_category_id,))

    books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'book_img':data[2],
            'publisher':data[3],
            'author':data[4],
            }
        books.append(row)

    return render(request, 'category_result.html', {'main_category':main,'books': books})