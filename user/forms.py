from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.exceptions import ValidationError

class CutomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def __init__(self, *args, **kwargs):
            super(CutomUserCreationForm, self).__init__(*args, **kwargs)

            for name, fields in self.fields.items():
                fields.widget.attrs.update({'class': 'input'})
    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
       return self.cleaned_data