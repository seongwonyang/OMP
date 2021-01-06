from django.urls import re_path
from .splitviews import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'

urlpatterns = [
    re_path(r'^$', MainView, name='main'),
    re_path(r'^bookstore/$', SearchStoreView, name='search_store'),
    re_path(r'^bookstore/region/$', RegionSearchView, name='region_search'),
    re_path(r'^bookstore/keyword/$', KeywordSearchView, name='keyword_search'),
    re_path(r'^bookstore/(?P<store_id>\d+)/$', BookStoreDetailView, name='bookstore_detail'),
    re_path(r'^book/$', SearchBookView, name='search_book'),
    re_path(r'^book-list/$', SearchBookResultView, name='search_book_result'),
    re_path(r'^mypage/$', MyPageView, name='mypage'),
    re_path(r'^ajax-city/$', AjaxGetCityView, name='ajax_get_city'),
    re_path(r'^book/(?P<book_isbn>\d+)/(?P<store_id>\d+)/$', BookDetailView, name='book_detail'),
    re_path(r'^book/(?P<book_isbn>\d+)/(?P<store_id>\d+)/customer/$', BookLikeView, name='book_like'),
    re_path(r'^favorite/(?P<store_id>\d+)/$', FavoriteView, name='favorite'),
    re_path(r'^unfavorite/(?P<store_id>\d+)/$', UnfavoriteView, name='unfavorite'),
    re_path(r'^review/(?P<book_isbn>\d+)/(?P<store_id>\d+)/$', BookReviewView, name='book_review'),
    re_path(r'^review/(?P<review_id>\d+)/user/$', BookReviewDeleteView, name='book_review_delete'),
    re_path(r'^review/(?P<review_id>\d+)/modify/$', BookReviewModifyView, name='book_review_modify'),
    re_path(r'^review-ajax-recent/(?P<book_isbn>\d+)/$', AjaxReviewRecentView, name='ajax_review_recent'),
    re_path(r'^review-ajax-highScore/(?P<book_isbn>\d+)/$', AjaxReviewHighScoreView, name='ajax_review_high_score'),
    re_path(r'^basket/(?P<book_isbn>\d+)/(?P<store_id>\d+)/$', BookBasketInsertView, name='book_basket_insert'),
    re_path(r'^basket/(?P<book_isbn>\d+)/session/$', BookBasketDeleteView, name='book_basket_delete'),
    re_path(r'^book/category/$', CategoryView, name='category'),
    re_path(r'^book/category/(?P<main_category_id>\d+)/$', CategoryResultView, name='category_book'),
    re_path(r'^order-sheet/(?P<book_isbn>\d+)/(?P<store_id>\d+)/$', OrderSheetView, name='order_sheet'),
    re_path(r'^order-sheet/cart/$', OrderSheetCartView, name='order_sheet_cart'),
    re_path(r'^order-sheet/create/$', OrderCreateView, name='order'),
    re_path(r'^order-confirm/(?P<order_num>\d+)/$', OrderConfirmView, name='order_confirm'),
    re_path(r'^order-detail/(?P<order_num>\d+)/$', OrderDetailView, name='order_detail'),
    re_path(r'^order-history/$', OrderHistoryView, name='order_history'),
    re_path(r'^bookstore/book-list/$', SearchBookInStoreView, name='search_book_in_store'),
    re_path(r'^mypage_basket/$', CustomerBasketView, name='mypage_basket'),
    re_path(r'^order-decision/(?P<order_num>\d+)/$', OrderDecisionView, name='order_decision'),
    re_path(r'^order-cancel/(?P<order_num>\d+)/$', OrderCancelView, name='order_cancel'),
    re_path(r'^product-return/(?P<order_id>\d+)/$', ProductReturnView, name='product_return'),
    re_path(r'^frequently-question/(?P<store_id>\d+)/$', FrequentQuestionView, name='frequent_question'),
    re_path(r'^individual-question/(?P<store_id>\d+)/$', IndividualQuestionView, name='individual_question'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)