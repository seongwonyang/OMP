from .common import *

@login_required
def NoticeForCustomerView(request):
    user = request.user
    id_sql = "SELECT id FROM bookstore WHERE seller_id = (%s)"
    store_id = execute_and_get(id_sql, (user,))

    if request.method == 'GET':
        notice_sql = "SELECT id, notice, date FROM notice WHERE store_id = (%s) ORDER BY date desc"

        datas = execute_and_get(notice_sql, (store_id[0][0],))

        notices = []
        for data in datas:
            row = {
                'notice_id': data[0],
                'notice': data[1],
                'date': data[2],
            }
            notices.append(row)

        return render(request, 'notice.html', {'notices': notices})

    elif request.method == 'POST':

        notice = request.POST.get('notice')
        notice_id = request.POST.get('notice_id')
        if len(notice_id) == 0:

            insert_sql = "INSERT INTO notice(store_id, notice) " \
                         "VALUES ((%s), (%s))"
            execute(insert_sql, (store_id[0][0], notice,))

        else:
            update_sql = "UPDATE notice SET notice = (%s) " \
                         "WHERE id = (%s)"
            execute(update_sql, (notice, notice_id))

        return redirect('seller:notice')