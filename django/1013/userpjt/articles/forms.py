from django import forms
from .models import Reviexs

class ReviewsForm(forms.ModelForm):
    
    class Meta:
        model = Reviexs
        fields = "__all__"
