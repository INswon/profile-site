from typing import Any
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "Shun"
        return ctxt
    

class LogoutView(TemplateView):
    template_name = "logout.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["skills"] = [
            "Python",
            "C++",
            "Javascript",
            "Rust",
            "Go",
        ]
