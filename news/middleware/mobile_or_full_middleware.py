class MobileOrFullMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        if 'Mobile' in user_agent:
            print("пользователь зашел с мобильного устройства")
        else:
            print("пользователь зашел с ПК")
        #response.template_name = prefix + response.template_name
        
        return response