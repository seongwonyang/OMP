from .common import *

def SearchStoreView (request):
    if request.method == "GET":
        strSql = "SELECT store_name, address FROM bookstore"

        storedata = execute_and_get(strSql)

        bookstores = []
        for data in storedata:
            row = {'store_name': data[0],
                   'address': data[1],
                   }
            json_row = json.dumps(row)
            bookstores.append(json_row)
        bookstores = json.dumps(bookstores)


        strSql = "SELECT province FROM province"

        datas = execute_and_get(strSql)

        provinces = []
        for data in datas:
            row = {'name': data[0],}
            provinces.append(row)

        return render(request, 'search_store.html', {'bookstores': bookstores,
                                                     'provinces': provinces})