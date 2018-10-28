from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
@ensure_csrf_cookie
def resultPage(request):
    #return HttpResponse('Hello, World!')
    #return redirect("")
    return render(request, 'results.html', {})
