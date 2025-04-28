from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def index(request):
    notes = Note.objects.filter(owner=request.user)
    print(notes)
    return render(request, 'index.html', {'notes' : notes})

def details(request, id1):
    note = Note.objects.get(id=id1)
    return render(request, 'details.html', {'note' : note})
