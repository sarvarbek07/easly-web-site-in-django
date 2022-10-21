
from django.forms import ModelForm
from .models import Blog

class Addform (ModelForm):
    class Meta:
        model=Blog
        fields=['title','text','after']