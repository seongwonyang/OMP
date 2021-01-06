from .common import *

@login_required
def FrequentQuestionDeleteView(request, faq_id):
    execute("DELETE FROM frequent_question WHERE id = (%s)", (faq_id,))
    return redirect('seller:frequent_question')