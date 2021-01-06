from .common import *

@login_required
def BookLikeView(request, book_isbn, store_id):
    user = request.user

    is_like = execute_and_get("SELECT exists (SELECT * FROM like_list WHERE user_id = (%s) AND book_isbn = (%s) AND store_id = (%s))",
                              (user.username, book_isbn, store_id,))

    if is_like[0][0] == False:
        execute("INSERT INTO like_list(user_id, book_isbn, store_id) VALUES ((%s), (%s), (%s))",
                           (user.username, book_isbn, store_id,))

    else:
        execute("DELETE FROM like_list WHERE user_id = (%s) AND book_isbn = (%s) AND store_id = (%s)",
                              (user.username, book_isbn, store_id,))

    update_is_like = execute_and_get("SELECT exists (SELECT * FROM like_list WHERE user_id = (%s) AND book_isbn = (%s) AND store_id = (%s))",
        (user.username, book_isbn, store_id,))

    return HttpResponse(json.dumps({'is_like': is_like[0][0], 'update_is_like': update_is_like[0][0]}), content_type="application/json")