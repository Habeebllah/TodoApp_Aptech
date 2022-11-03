from django.shortcuts import render

# Create your views here.
def Home(request):
    template_name = 'index.html'
    return render(request, template_name)


def Contact(request):
    template_name = 'contact.html'
    return render(request, template_name)