from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class Login(LoginView, SuccessMessageMixin):
    template_name = "account/auth.html"
    redirect_authenticated_user = True
    success_message = "UrbanGeoSIG - Sessão iniciada com sucesso!"


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(
            request,
            messages.INFO,
            "UrbanGeoSIG - Sua sessão foi encerrada com sucesso!",
        )
        return response


login = Login.as_view()
logout = Logout.as_view()
