from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^download/$', views.download, name='download'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^features/$', views.features, name='features'),
    url(r'^$', views.index, name=''),
    url(r'^login/$', views.login, name='login'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^review/$', views.review, name='review'),
    url(r'^index_after/$', views.index_after, name='index_after'),
    url(r'^study/$', views.study, name='study'),
    url(r'^study_six/$', views.study_six, name='study_six'),
    url(r'^study_toefl/$', views.study_toefl, name='study_toefl'),
    url(r'^note/$', views.note, name='note'),
    url(r'^review_four/$', views.review_four, name='review_four'),
    url(r'^review_six/$', views.review_six, name='review_six'),
    url(r'^review_toefl/$', views.review_toefl, name='review_toefl'),
    url(r'^test_four/$', views.test_four, name='test_four'),
    url(r'^test_six/$', views.test_six, name='test_six'),
    url(r'^test_toefl/$', views.test_toefl, name='test_toefl')
]