from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import Group


def createPost(allow=[]):
    def dec(view_func):
        def wrapper(request, *args, **kwargs):
            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group in allow:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(f"Sorry!You can't do this")   
        return wrapper
    return dec
