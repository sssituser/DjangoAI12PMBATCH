class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        print('Init Method Execution')
        self.get_response = get_response
        
    def __call__(self, request):
        print('Preprocessing of the Request')
        response = self.get_response(request)
        print('PostProcessing of the  request')
        return response
    
        