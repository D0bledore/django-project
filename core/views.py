from django.shortcuts import render

# Create your views here.
def core_index(request):
    return render(request, 'core/index.html')


def core_about(request):
    return render(request, 'core/about.html')


def core_contact(request):
    return render(request, 'core/contact.html')

