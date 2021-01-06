from .common import *

@login_required
def InfoManageView(request):
    tab_is = 0

    return render(request, 'info_manage.html', {'tab_is': tab_is} )