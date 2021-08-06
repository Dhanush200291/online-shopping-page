from django.forms import ModelForm
from .models import user,product
class wishlist(ModelForm):
    class Meta:
        model = user
        fields = '__all__'