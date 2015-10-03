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
url(r'^users/$', views.UserList.as_view()),
url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
url(r'^questions/$', views.QuestionList.as_view()),
url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
url(r'^answers/$', views.AnswerList.as_view()),
url(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerDetail.as_view()),
)