from .common import *

@require_POST
def AjaxGetCityView(request):

    province_name = request.POST.get('province_name')

    strSql = "SELECT city"
    strSql += " FROM city"
    strSql += " JOIN province ON province.id = city.province_id"
    strSql += " WHERE province = (%s)"

    datas = execute_and_get(strSql, (province_name,))

    cities = []
    for data in datas:
        raw_dict = {
            "name": data[0],
        }

        cities.append(raw_dict)

    return HttpResponse(json.dumps({'cities': cities}), content_type="application/json")
