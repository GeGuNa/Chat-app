#from django.utils.deprecation import MiddlewareMixin


#class MyMiddleware(MiddlewareMixin):
class MyMiddleware:
    def __init__(self, get_response):
        #self.test = "qweqwe"
        self.get_response = get_response
         
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # This is similar to before_request in Flask.
        
        #if 'xz' in request.session:
        request.session['xz'] = "attest"
           
        
        #print("before response")
        response = self.get_response(request)
        #print("After response")



        # Code to be executed for each request/response after
        # the view is called.

        return response
