from django.urls import re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'seller'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^product/$', ProductListView, name='product_list'),
    re_path(r'^product/book-list$', SearchBookInManageView, name='search_book_in_manage'),
    re_path(r'^product/book-delete/(?P<store_id>\d+)/(?P<isbn>\d+)/$', ProductDeleteView, name='book_delete'),
    re_path(r'^product-modify/$', ProductModifyView, name='book_modify'),
    re_path(r'^product-modify-ajax/(?P<isbn>\d+)/$', AjaxGetProductInfoView, name='book_modify_ajax'),
    re_path(r'^product-register/$', ProductRegisterView, name='product_register'),
    re_path(r'^book-ajax/$', SearchBookAjaxView, name='ajax_book_search'),
    re_path(r'^order/$', OrderCheckView, name='order_check'),
    re_path(r'^pay-check-ajax/(?P<order_num>\d+)/$', PayCheckAjaxView, name='pay_check_ajax'),
    re_path(r'^order-detail-ajax/(?P<order_num>\d+)/$', OrderDetailView, name='order_detail_ajax'),
    re_path(r'^order-return/(?P<click_case>[ㄱ-힣a-zA-Z0-9-_.]*)/$', OrderReturnView, name='order_return'),
    re_path(r'^order-return-check-ajax/(?P<return_id>\d+)/$', OrderReturnCheckAjaxView, name='order_return_check_ajax'),
    re_path(r'^order-return-reject/(?P<return_id>\d+)/$', OrderReturnRejectView, name='order_return_reject'),
    re_path(r'^order-return-reject-compl-ajax/(?P<return_id>\d+)/$', OrderReturnRejectCompAjaxlView, name='order_return_reject_compl_ajax'),
    re_path(r'^book-register/$', BookRegisterView, name='book_register'),
    re_path(r'^delivery/$', DeliveryCheckView, name='delivery_check'),
    re_path(r'^delivery-ajax/(?P<order_num>\d+)/$', DeliveryCheckAjaxView, name='delivery_check_ajax'),
    re_path(r'^notice/$', NoticeForCustomerView, name='notice'),
    re_path(r'^notice-delete/(?P<notice_id>\d+)/$', NoticeDeleteView, name='notice_delete'),
    re_path(r'^notice-modify-ajax/(?P<notice_id>\d+)/$', AjaxGetNoticeView, name='notice_modify_ajax'),
    re_path(r'^settlement/$', SettlementCheckView, name='settlement_check'),
    re_path(r'^monthly-settlement/$', MonthlySettlementView, name='monthly_settlement'),
    re_path(r'^frequent-question/$', FrequentQuestionView, name='frequent_question'),
    re_path(r'^frequent-question-delete/(?P<faq_id>\d+)/$', FrequentQuestionDeleteView, name='frequent_question_delete'),
    re_path(r'^frequent-question-modify/(?P<faq_id>\d+)/$', FrequentQuestionModifyView, name='frequent_question_modify'),
    re_path(r'^individual-question/(?P<store_id>\d+)/$', IndividualQuestionView, name='individual_question'),
    re_path(r'^individual-question-answer/(?P<question_id>\d+)/$', IndividualQuestionAnswerView, name='individual_question_answer'),
    re_path(r'^review/$', ReviewManageView, name='review_manage'),
    re_path(r'^review-answer/$', ReviewAnswerView, name='review_answer'),
    re_path(r'^review-answer-ajax/(?P<review_id>\d+)/$', AjaxGetReviewAnswerView, name='answer_modify_ajax'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
