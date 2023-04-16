from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Callback


class CallbackCreateView(CreateView):
    model = Callback
    fields = ['customer_email', 'customer_phone', 'customer_name', 'id_product', 'message']
    success_url = reverse_lazy('home')  # url, куда перенаправится пользователь после успешного создания объекта

    def form_valid(self, form):
        form.instance.checked = False  # устанавливаем значение поля "checked" в False
        return super().form_valid(form)
