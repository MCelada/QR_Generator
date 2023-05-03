from django import forms
from generator.models import Wifi
    
class WifiForm(forms.ModelForm):
    class Meta:
        model = Wifi
        fields = ('ssid','security','password',)