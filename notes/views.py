from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def index(request):
    #return render(request, 'index.html')
    return render(request, 'index.html', {'user' : request.user})

#@login_required
def notes(request, id):
#def notes(request):
    #notes = Note.objects.filter(owner=request.user)
    query = 'SELECT * FROM notes_note WHERE owner_id = %s' % id
    notes = Note.objects.raw(query)

    return render(request, 'notes.html', {'notes' : notes})

#@login_required
#def details(request, id1):
#    note = Note.objects.get(id=id1)
#    if (note.owner == request.user):
#        return render(request, 'details.html', {'note' : note})
#    else:
#        return HttpResponseNotFound("<h1>Page not found</h1>")

@login_required
def addView(request, id):
	if (request.method == 'POST'):
		Note.objects.create(owner=request.user, note=request.POST.get('note'), description=request.POST.get('description'))
	return redirect('/notes/' + id)
