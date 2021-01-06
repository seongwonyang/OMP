from .common import *

@login_required

def UnfavoriteView(request, store_id):
    user = request.user

    strSql = "DELETE FROM favorite_bookstore "
    strSql += "WHERE user_id=(%s) and bookstore_id = (%s)"

    execute(strSql, (user.username, store_id,))

    return HttpResponse(json.dumps({'result':'200'}), content_type="application/json")