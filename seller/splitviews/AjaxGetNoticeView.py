from .common import *

@login_required
def AjaxGetNoticeView(request, notice_id):

    notice_sql = "SELECT notice FROM notice WHERE id=(%s)"
    data = execute_and_get(notice_sql, (notice_id,))

    notice_info = {'notice': data[0][0],
                   'notice_id': notice_id,}

    return HttpResponse(json.dumps({'notice_info': notice_info}), content_type="application/json")