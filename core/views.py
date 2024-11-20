from django.shortcuts import render

# Create your views here.
def core_index(request):
    return render(request, 'core/index.html')