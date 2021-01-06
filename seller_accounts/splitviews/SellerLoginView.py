from .common import *

def SellerLoginView(request):
    if request.method == "GET":
        return render(request, 'seller_login.html')