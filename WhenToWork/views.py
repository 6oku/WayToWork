from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from .models import Document, List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def editor(request):
    docid = int(request.GET.get('docid', 0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
        user = request.user

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()
            document.user = request.user
            request.user.notepadname.add(document)

            return redirect('./?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content, user = user)

            return redirect('./?docid=%i' % docid)
    if docid > 0:
        document = Document.objects.get(pk=docid)
    else:
        document = ''

    context = {
        'docid': docid,
        'documents': documents,
        'document': document
    }

    return render(request, 'editor.html', context)

def delete_document(request, docid):
    document = Document.objects.get(pk=docid)
    document.delete()

    return redirect(editor)

def todo(request):
    all_items = List.objects.all

    if request.method == 'POST':
       form = ListForm(request.POST)
       user = request.user
       
    #    List.item = request.POST.get('item', '')
    #    List.completed = request.POST.get('completed')

       if form.is_valid():
           n = form.cleaned_data["item"]
           t=List(item=n)
           t.save
           request.user.todolist.add(t,bulk=False)

           all_items = List.objects.all

           messages.success(request, ('Item Has Been Added To List!'))
           return render(request, 'todo.html', {'all_items': all_items})

    else:
        all_items = List.objects.all
        return render(request, 'todo.html', {'all_items': all_items})

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ("Item Has Been Deleted!"))
    return redirect('todo')

def cross_off(request, list_id):
    item= List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo')

def uncross(request, list_id):
    item= List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo')

def dashboard(request):
    return render(request, 'dashboard.html')

def viewPage(response):
    return render(response, 'view.html')


def timer(request):
        return render(request, 'timer.html')