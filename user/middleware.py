from localStoragePy import localStoragePy


def init_session(get_response):
    def middleware(request):
        localStorage = localStoragePy('photo', 'postgresql')
        

        if request.POST.get('session_key'):
            localStorage.setItem('session_key', request.POST.get('session_key'))

        return get_response(request)

    return middleware
