from django.shortcuts import render

# Create your views here.

def resultsPage(request):
    if request.method == 'POST':
            return HttpResponseRedirect('http://cnn.com')
    else:
        print('OUTPUTTING RESULTS TABLE')
    
        return render(request, 'results.html', {'form': form,})
