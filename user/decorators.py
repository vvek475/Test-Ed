from django.shortcuts import redirect

def authenticatedRedirect(view_func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect(request.session.get('url',request.path))
        else:
            return view_func(request,*args,**kwargs)
    return wrapper