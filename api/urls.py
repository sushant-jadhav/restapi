# from django.conf.urls import url,patterns
# from rest_framework.urlpatterns import format_suffix_patterns
# from api import views

# urlpatterns = patterns(
#     'api.views',
#     url(r'^ques/$', 'question_list', name='question_list'),
#     url(r'^ques/(?P<pk>[0-9]+)$', 'question_detail', name='question_detail'),
# )
# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views
# admin.autodiscover()
urlpatterns = patterns('',
#url(r'^', include(router.urls)),
url(r'^admin/', include(admin.site.urls)),
url(r'^users/$', views.UserList.as_view(),name='user-list'),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='user-details'),
url(r'^questions/$', views.QuestionList.as_view(),name='question-list'),
url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(),name='question_detail'),
url(r'^answers/$', views.AnswerList.as_view(),name='answer_list'),
url(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerDetail.as_view(),name='answer_detail'),
url(r'^likes/$', views.LikeList.as_view(),name='like-list'),
url(r'^likes/(?P<pk>[0-9]+)/$', views.LikeDetail.as_view(),name='like-detail'),
)