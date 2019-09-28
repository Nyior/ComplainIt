from django.urls import path
#from .views import home_view
from . import views
from .views import (home_view, 
                    complainStatus_view,
                    ComplainCreateView,
                    PostListView,
                    agency_login_view
)



urlpatterns = [
    #path('', home_view, name = 'home'),
    path ('complainStatus/', complainStatus_view, name = 'complain-status'),
    path('complain/', ComplainCreateView.as_view(), name = 'complain-create'),
    path('agencylogin/', agency_login_view, name = 'agency-login'),
    path('', PostListView.as_view(), name = 'home')

]