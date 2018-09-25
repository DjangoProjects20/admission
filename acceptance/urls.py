from django.conf.urls import url, include
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^form_email/$', views.form_email, name='form_email'),
url(r'^generator$', views.time_acceptance_period_page, name='generator'),
url(r'^admission_page/(?P<admission_id>\w+)/$', views.admission_one, name='admission_page'),
url(r'^priem$', views.priem, name='priem'),
url(r'^post_one/(?P<post_id>\w+)/$', views.post_one_page, name='post_one'),
]