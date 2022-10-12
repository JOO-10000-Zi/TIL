
from django import forms
from .models import Reviews

class ReviewsFrom(forms.ModelForm):
    
    class Meta:
        model = Reviews
        fields = "__all__"
