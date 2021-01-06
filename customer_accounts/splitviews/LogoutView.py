from .common import *

def LogoutView(request):
    logout(request)
    return redirect('customer:main')