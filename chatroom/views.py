from django.shortcuts import render
from .models import massage
from .mixins import FormValidMixin
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    context = {
        'message': massage.objects.all()
    }
    return render(request, 'index.html', context)

class massageCreateView(CreateView, FormValidMixin):
    model = massage
    fields = ['matnpayam', 'athor']
    template_name = "gh.html"
