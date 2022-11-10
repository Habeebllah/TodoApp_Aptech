from django.shortcuts import render, redirect
from app.forms import TodoForm
from app.models import Todo

# Create your views here.
def Home(request):
    template_name = 'index.html'
    items = Todo.objects.all()
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        'form': form,
        'items': items
    }
    return render(request, template_name, context)

def DeleteItem(request, id):
    print(id)
    item = Todo.objects.get(id=id)
    item.delete()
    return redirect("/")

def Contact(request):
    template_name = 'contact.html'
    return render(request, template_name)