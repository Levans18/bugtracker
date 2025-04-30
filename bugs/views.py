from django.shortcuts import render, redirect, get_object_or_404
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

def delete_bug(requrest, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)
    bug.delete()
    return redirect('bug_list')