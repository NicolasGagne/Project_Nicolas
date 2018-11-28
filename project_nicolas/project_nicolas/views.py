from django.shortcuts import render, redirect
from rest_framework.reverse import reverse




def bare(request):
    return redirect(reverse('index'))

def index(request):
    """
    View is the project base view, include link to orther project.
    """
    context = {

    }
    return render(request, 'index.html', context)


def AppBookmarks_root(request):
    """
    View is the first page for App bookmarks
    """
    context = {

    }
    return render(request, 'appbookmarks_root.html', context)
