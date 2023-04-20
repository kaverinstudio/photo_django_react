from localStoragePy import localStoragePy


def init_session(get_response):
    def middleware(request):
        localStorage = localStoragePy('photo', 'postgresql')
        session_key = localStorage.getItem('session_key')

        if request.POST.get('session_key') is not None:
            localStorage.setItem('session_key', request.POST.get('session_key'))

        return get_response(request)

    return middleware
