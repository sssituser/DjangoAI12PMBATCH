class SecondMiddleware(object):
    def __init__(self,get_response):
        print("SecondMiddlewareExecuted")
        self.get_response = get_response
        
    def __call__(self,request):
        print("Middleware-2 before processing request")
        response = self.get_response(request)
        print("Middleware-2 Afer Proccesing request(response)")
        return response
