from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, full_name, email, password=None, **kwargs):
        user = self.model(full_name=full_name, email=email, **kwargs)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self.db)
        return user
    
    def create_superuser(self, full_name, email, password=None, **kwargs):
        kwargs.update({ 'is_staff': True, 'is_superuser': True, 'is_active': True })
        return self.create_user(full_name, email , password, **kwargs)