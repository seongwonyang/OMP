from .common import *

def SearchBookAjaxView(request):
    title = request.GET.get('search_book_name')
    publisher = request.GET.get('search_book_publisher')
    author = request.GET.get('search_author')

    search_datas = execute_and_get("SELECT isbn, book_name, author, publisher FROM book " +
                   " WHERE book_name LIKE '%" + title + "%' AND publisher LIKE '%" + publisher + "%' AND author LIKE '%" + author + "%'")

    registered_book = 1
    if len(search_datas) == 0:
        registered_book = 0
    elif title == "" and author == "" and publisher == "":
        registered_book = -1

    search_result = []
    for search_data in search_datas:
        data = {'isbn': search_data[0],
                'book_name': search_data[1],
                'author': search_data[2],
                'publisher': search_data[3],}
        search_result.append(data)

    return HttpResponse(json.dumps({'search_result': search_result, 'registered_book': registered_book}), content_type="application/json")