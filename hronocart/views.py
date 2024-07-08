from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# Create your views here.

from django.views import View


class main_window(View):
    def get(self, request):
        return render(request, 'demo.html')


# Create your views here.
