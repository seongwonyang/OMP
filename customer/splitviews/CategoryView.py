from .common import *

def CategoryView (request):
    strSql = "SELECT id, main_category FROM main_category WHERE origin ='국내도서'"

    datas = execute_and_get(strSql)

    domestic = []
    for data in datas:
        row = {
            'main_category_id': data[0],
            'main_category':data[1],
        }
        domestic.append(row)

    strSql = "SELECT id, main_category FROM main_category WHERE origin ='외국도서'"

    datas = execute_and_get(strSql)

    foreign = []
    for data in datas:
        row = {
            'main_category_id': data[0],
            'main_category':data[1],
        }
        foreign.append(row)

    domestic_bookSql = "SELECT distinct a.isbn, a.book_name, a.book_img, a.publisher, a.author "\
                       "FROM book AS a "\
                       "JOIN main_category AS b "\
                       "ON a.category_id = b.id " \
                       "JOIN book_inven AS c " \
                       "ON a.isbn = c.book_isbn "\
                       "WHERE b.origin = '국내도서'"

    datas = execute_and_get(domestic_bookSql)

    domestic_books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'book_img':data[2],
            'publisher':data[3],
            'author':data[4],
            }
        domestic_books.append(row)

    foreign_bookSql = "SELECT distinct a.isbn, a.book_name, a.book_img, a.publisher, a.author "\
                      "FROM book AS a "\
                      "JOIN main_category AS b " \
                      "ON a.category_id = b.id " \
                      "JOIN book_inven AS c " \
                      "ON a.isbn = c.book_isbn " \
                      "WHERE b.origin = '외국도서'"

    datas = execute_and_get(foreign_bookSql)

    foreign_books = []
    for data in datas:
        row = {
            'isbn':data[0],
            'book_name':data[1],
            'book_img':data[2],
            'publisher':data[3],
            'author':data[4],
            }
        foreign_books.append(row)

    return render(request, 'category.html', {'domestic':domestic,'foreign': foreign,
                                             'domestic_books':domestic_books, 'foreign_books':foreign_books})