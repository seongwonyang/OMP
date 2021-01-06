from .common import *

def KeywordSearchView (request):
    if request.method == "POST":
        keyword = request.POST.get("search_store")

        nameSql = "SELECT store_name, address"
        nameSql += " FROM bookstore"
        nameSql += " WHERE store_name LIKE '%" + keyword + "%'"

        namedata = execute_and_get(nameSql)

        if len(namedata) == 0:
            messages.error(request, '아직 등록되지 않은 서점입니다.')
            return redirect('customer:search_store')

        else:

            bookstores = []
            for data in namedata:
                row = {'store_name': data[0],
                       'address': data[1],
                       }
                json_row = json.dumps(row)
                bookstores.append(json_row)
            bookstores = json.dumps(bookstores)

            idSql = "SELECT id, store_name, address"
            idSql += " FROM bookstore"
            idSql += " WHERE store_name LIKE '%" + keyword + "%'"

            listdata = execute_and_get(idSql)

            liststores = []
            for data in listdata:
                row = {'store_id': data[0],
                       'store_name': data[1],
                       'address': data[2],
                       }
                liststores.append(row)

            strSql = "SELECT province FROM province"

            datas = execute_and_get(strSql)

            provinces = []
            for data in datas:
                row = {'name': data[0], }
                provinces.append(row)

            return render(request, 'search_store.html', {'bookstores': bookstores,
                                                         'liststores': liststores,
                                                         'provinces': provinces})
