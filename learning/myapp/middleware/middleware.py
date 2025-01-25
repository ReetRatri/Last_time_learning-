from django.http import HttpResponseForbidden

Allowed_ip = ["123.23.23.23" , "123.23.23.24"]
class ipBlockingMiddleware:
    # init
    # process request 
    # process view  ,
    # process response 
    # process exception

    

        
    def __init__(self , get_response)->None:
        self.get_response = get_response

    def get_client_ip(self , request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
           
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('x_forwarded_for')
        return ip 
        

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        print("=======================================")
        print("=======================================")
        print("=======================================")
        print("=======================================")
        print("=======================================")
        print("=======================================")
        if ip in Allowed_ip:
            return HttpResponseForbidden('IP not allowed')
        
        return self.get_response(request)


     