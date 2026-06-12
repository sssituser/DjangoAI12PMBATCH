from django.http import HttpResponse
class AppMaintainenceMiddleware(object):
    def __init__(self,get_responce):
        print("Init Method Executed")
        self.get_responce=get_responce
    def __call__(self, request):
        print("Pre Request Processed")
        response = self.get_responce(request)
       # return HttpResponse("<h1>Currently Application under maintainence Try after two days</h1>")
        print("Post Requset Processed , Responce")
        return response