from django.shortcuts import render, redirect
from .models import Bug
from .forms import BugForm

# Create your views here.
def bug_list(request):
    bugs = Bug.objects.all().order_by('-created_at')
    return render(request, 'bugs/bug_list.html', {'bugs': bugs})


def create_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm()

    return render(request, 'bugs/create_bug.html', {'form': form})