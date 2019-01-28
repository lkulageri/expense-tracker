
from . import views


from django.conf.urls import url


# SET THE NAMESPACE!
app_name = 'expenses'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^add/$',views.add,name='add'),
    url(r'^home/$',views.home,name='home'),
    url(r'^viewlist/$',views.viewlist,name='viewlist'),
    url(r'^(?P<p_k>\d+)/modify/', views.modify, name='modify'),
    url(r'^itemupdate/(?P<p_k>\d+)/', views.itemupdate, name='itemupdate'),
    url(r'^itemdelete/(?P<p_k>\d+)/$', views.itemdelete, name='itemdelete'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]