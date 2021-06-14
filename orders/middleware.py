from .models import Logs


# HT 9. Middleware, ModelAdmin
class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        method = request.method
        # if 'admin' not in path:
        if not request.path.startswith('/admin'):
            Logs.objects.create(path=path, method=method)
        response = self.get_response(request)
        return response
