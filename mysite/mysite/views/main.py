from django.http import HttpResponse
from django.views.generic.base import TemplateView

def my_view(request):
    # ...

    # Return a "created" (201) response code.
    return HttpResponse(status=201)

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context