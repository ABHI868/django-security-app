from django.conf.urls import url
from .import views

app_name='Sangaria'
urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^form/$',views.form,name='form'),
    url(r'^submit/$',views.submit,name='submit'),
    url(r'^final/$',views.home,name='home'),
    #url(r'^form/$',views.Visitors_detail_view,name="form_view"),
    url(r'^form1/$',views.Visitors_detail_view1,name="form_view_raw"),
    url(r'^modelform/$',views.maintenance_modelform_view,name="maintenance_view"),
    url(r'^createview/$',views.createviewpublic.as_view(),name="createview"),
    url(r'^updateview/<int:id>/$' ,views.updateviewpublic.as_view(),name="updateview"),




]