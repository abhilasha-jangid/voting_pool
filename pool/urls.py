from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.index,name='index'),
    url(r'^details/(?P<id>\d+)/$',views.details,name="details"),
    url(r'^submitVote/(?P<pid>\d+)/(?P<oid>\d+)/$',views.submit,name="submit"),
    url(r'^signup/$', views.signup, name='signup'),

]