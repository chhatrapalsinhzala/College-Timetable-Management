from .views import CreateClassView, SubjectView
from django.conf.urls import url

urlpatterns = [
    url('create-class/', CreateClassView.as_view(),name = "create_class"),
    url('subject/', SubjectView.as_view(),name = "subject"),

]
app_name = 'classapp'