from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# UserCreationForm, UserChangeForm 오버라이딩
class CustomUserCreationForm(UserCreationForm):
    
    #Meta클래스의 model만 변경해주면 됨
    #models의 User class를 가져와도 되지만 get_user_model메서드의 사용 권장
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model=get_user_model()
        fields=('username', 'email', 'first_name', 'last_name',)