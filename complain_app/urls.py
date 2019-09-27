from django.urls import path
#from .views import home_view
from . import views
from .views import (home_view, 
                    complainStatus_view,
                    ComplainCreateView,
                    PostListView,
                    AgencyLoginView
)



urlpatterns = [
    #path('', home_view, name = 'home'),
    path ('complainStatus/', complainStatus_view, name = 'complain-status'),
    path('complain/', ComplainCreateView.as_view(), name = 'complain-create'),
    path('agencylogin/', AgencyLoginView, name = 'agency-login'),
    path('', PostListView.as_view(), name = 'home')

]