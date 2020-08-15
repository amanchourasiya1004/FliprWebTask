from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style = {'input_type' : 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    def save(self):
        password = self.validated_data['password']
        # password1 = self.validated_data['password1']
        # if(password != password1):
        #     raise serializers.ValidationError({'password' : 'Passwords must match.'})
        account = User.objects.create_user(username = self.validated_data['username'], email = self.validated_data['email'])
        account.set_password(password)
        account.save()
        return account