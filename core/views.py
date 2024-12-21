from django.shortcuts import render, redirect
from django.contrib import messages


# View to render the core index page
def core_index(request):
    return render(request, 'core/index.html')


# View to render the core contact page
def core_contact(request):
    if request.method == 'POST':
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('index')
    return render(request, 'core/contact.html')
