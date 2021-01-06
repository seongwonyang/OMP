from .common import *

@login_required

def FavoriteView(request, store_id):
    user = request.user

    strSql = "INSERT INTO favorite_bookstore(user_id, bookstore_id) "
    strSql+= "VALUES((%s), (%s))"

    execute(strSql, (user.username, store_id,))

    return HttpResponse(json.dumps({'result':'200'}), content_type="application/json")