from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def index(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, 'index.html', {'notes' : notes})

def details(request, id1):
    #note = Note.objects.get(id=id1)
    query = 'SELECT * FROM notes_note WHERE id = %s' % id1
    note = Note.objects.raw(query)[0]

    return render(request, 'details.html', {'note' : note})

#@login_required
#def details(request, id1):
#    note = Note.objects.get(id=id1)
#    if (note.owner == request.user):
#        return render(request, 'details.html', {'note' : note})
#    else:
#        return HttpResponseNotFound("<h1>Page not found</h1>")

@login_required
def addView(request):
	if (request.method == 'POST'):
		Note.objects.create(owner=request.user, note=request.POST.get('note'), description=request.POST.get('description'))
	return redirect('/')
