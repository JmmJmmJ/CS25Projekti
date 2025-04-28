from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def index(request):
    notes = Note.objects.filter(owner=request.user)

    return render(request, 'index.html', {'notes' : notes})
