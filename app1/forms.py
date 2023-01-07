from django.contrib.auth.forms import UserCreationForm

from app1.models import Login


class Form(UserCreationForm):
    class Meta:
        model = Login
        fields = ('username','name','email','contact_no','photo','password1','password2')

