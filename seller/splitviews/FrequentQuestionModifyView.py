from .common import *

@login_required
def FrequentQuestionModifyView(request, faq_id):
    user = request.user
    store_id = execute_and_get("SELECT id FROM bookstore WHERE seller_id = (%s)", (user.username,))

    title = request.POST.get('modal_title')
    content = request.POST.get('modal_content')

    execute_and_get("UPDATE frequent_question SET title = (%s), content = (%s) WHERE id = (%s)",
                    (title, content, faq_id,))

    return redirect('seller:frequent_question')