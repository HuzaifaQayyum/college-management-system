from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserUpdateForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
