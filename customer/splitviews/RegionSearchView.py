from .common import *

def RegionSearchView (request):
    if request.method == "POST":

        city = request.POST.get("city")
        province = request.POST.get('province')

        strSql = "SELECT store_name, address"
        strSql += " FROM bookstore"
        strSql += " WHERE address LIKE '" + province + "%" + city + "%'"

        idSql = "SELECT id, store_name, address"
        idSql += " FROM bookstore"
        idSql += " WHERE address LIKE '" + province + "%" + city + "%'"

        citydata = execute_and_get(strSql)

        listdata = execute_and_get(idSql)

        if len(citydata) == 0:
            messages.error(request, '해당지역에 등록된 서점이 없습니다.')
            return redirect('customer:search_store')

        else:

            bookstores = []
            for data in citydata:
                row = {'store_name': data[0],
                       'address': data[1],
                       }
                json_row = json.dumps(row)
                bookstores.append(json_row)
            bookstores = json.dumps(bookstores)

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
                                                         'liststores':liststores,
                                                         'provinces': provinces})