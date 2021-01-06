from .common import *

@login_required
def NoticeDeleteView(request, notice_id):

    execute("DELETE FROM notice WHERE id = (%s)", (notice_id,))

    return redirect('seller:notice')