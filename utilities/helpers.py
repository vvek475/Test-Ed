import json
from django.shortcuts import redirect


def formerrorsHandler(data):
    errors=dict(json.loads(data.as_json()))
    errorstr=list(errors.items())[0]
    return f"{errorstr[0]} : {errorstr[1][0]['message']}"

def setRedirectUrl(func):
    def wrapper(request,*args,**kwargs):
        data=func(request,*args,**kwargs)
        request.session['url']=request.path
        return data
    return wrapper

def unAuthorizedRedirect(allowedRoles=[]):
    def decorator(func):
        def wrapper(request,*args,**kwargs):
            if request.user.is_authenticated:
                if request.user.groups:
                    group=request.user.groups.all()[0]
                    if group.name in allowedRoles:
                        return func(request,*args,**kwargs)
                    else:
                        return redirect(request.session.get('url',request.path))
                else:
                    return redirect('login')
            else:
                return redirect('login')
        return wrapper
    return decorator