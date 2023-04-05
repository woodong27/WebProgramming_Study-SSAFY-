from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=get_user_model()
        #userchangeform에서 제공하는 field들 중에서 바꾸고 싶은 field만 표시
        fields=('username', 'email',)