class ExMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("My middleware #################")
        response = self.get_response(request)
        user_agent = request.META.get("HTTP_USER_AGENT")
        print("#####", user_agent)
        return response
