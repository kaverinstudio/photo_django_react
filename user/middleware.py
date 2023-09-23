from localStoragePy import localStoragePy
import json

def init_session(get_response):
    def middleware(request):
        localStorage = localStoragePy('photo', 'postgresql')

        if request.method == 'POST':
            try:

                data = json.loads(request.body)
                session_key = data.get("session_key")

                if session_key:
                    localStorage.setItem('session_key', session_key)
                else:
                    #log = open("log.txt", "w")
                    #log.write(str('else'))
                    #log.close()
                    pass
            except json.JSONDecodeError:
                #log = open("log.txt", "w")
                #log.write(str('exept'))
                #log.close()
                pass

        return get_response(request)

    return middleware
