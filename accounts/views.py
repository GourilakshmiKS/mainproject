from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request):
        title = "Welcome to the Best Online Event Ticketing System "
        context = {'title': title}
        return render(request,'common/index.html',context)