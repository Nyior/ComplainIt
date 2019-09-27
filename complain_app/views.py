from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from .models import Complain, Status, Post, MinedData, Agencies
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.

def home_view(request):
    return render(request, "complain_app/home.html", context=None)

def complainStatus_view(request):
    query = request.GET.get('password', None)
   

    if( request.method == 'GET'):
        complains = Complain.objects.filter(passcode=query)
        paginator = Paginator(complains, 2)
       
    return render(request, "complain_app/complainCheck.html", {'complains' : complains})

class ComplainCreateView(SuccessMessageMixin, CreateView):
    model = Complain
    fields = ['passcode', 'state', 'crime_type', 'agency', 'description']
    success_message = "Your complain was successfully launched. to check status of your complain, use your pascode: %(passcode)s "

    def form_valid(self, form):
        form.instance.status = Status.objects.get(id = 1)
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'complain_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['minedata'] = MinedData.objects.latest('id')
        return context

class UserComplainListView(ListView):
    model = Complain
    template_name = 'complain_app/complainCheck.html'
    context_object_name = 'complains '
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posed')

def AgencyLoginView():
    model = Agencies
    fields = ['name', 'password', 'state']
    template_name = 'complain_app/agencylogin.html'

    def form_valid(self, form):
        form.instance.status = Status.objects.get(id = 1)
        return super().form_valid(form)