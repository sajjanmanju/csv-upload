#from django.contrib import admin
#from .models import Product
from models import User #you can use get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import forms
from .models import Product

class MyUserCreationForm(UserCreationForm):
    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    class Meta(UserCreationForm.Meta):
        model = User

class MyUserAdmin(UserAdmin):  
    add_form = MyUserCreationForm   

admin.site.register(User,Product)
#admin.site.register(Product)
