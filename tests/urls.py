from allauth.socialaccount.forms import SignupForm
from allauth.socialaccount.models import SocialLogin
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import include, path
from django.views.generic.base import TemplateView

User = get_user_model()


class FakeSocialSignup(TemplateView):
    template_name = "socialaccount/signup.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fake_sociallogin = SocialLogin(user=User.objects.first())
        context["form"] = SignupForm(sociallogin=fake_sociallogin)
        return context


urlpatterns = [
    path("admin/", admin.site.urls),
    path("fake/accounts/social/signup", FakeSocialSignup.as_view()),
    path("accounts/", include("allauth.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
]
