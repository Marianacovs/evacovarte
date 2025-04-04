from django import forms
from.models import Contacto

# declara el formularion con python y asi encapsular las validaciones
class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields=['nombre','correo','mensaje','avisos']  
        # fields='__all__'   colocando all no es necesario hacer esto