from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class CreationForm(UserCreationForm):
    email = forms.EmailField(label="Ваша почта", required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        labels = {
            'username': "Логин",
            'password1': "Пароль",
            'password2': "Подтверждение пароля",
        }
        fields = ('username', 'email', 'password1', 'password2')
        # Сделай проверку подтверждения пароля и юзернейм только английскими буквами