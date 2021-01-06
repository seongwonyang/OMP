from .common import *

@login_required
def CustomerBasketView(request):
    tab = 'basket'
    return render(request, 'mypage.html', {'tab': tab})