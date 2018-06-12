from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def systemIndex(request):
    return render(request, 'system_index.html', {} )
