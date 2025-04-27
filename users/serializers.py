from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.password_validation import validate_password

# Serializer for registering a new user with additional profile information
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    date_of_birth = serializers.DateField(write_only=True, required=False)
    gender = serializers.ChoiceField(choices=(("Male", "Male"), ("Female", "Female"), ("Others", "Others")), write_only=True, required=False)
    phone = serializers.CharField(write_only=True, required=False)
    address = serializers.CharField(write_only=True, required=False)
    profile_picture = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'password', 'password2', 'date_of_birth', 'gender',
            'phone', 'address', 'profile_picture'
        )

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        # Extract profile-related fields
        extra_fields = {
            field: validated_data.pop(field)
            for field in ['date_of_birth', 'gender', 'phone', 'address', 'profile_picture']
            if field in validated_data
        }

        # Create user
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()

        # Update auto-created profile
        profile = user.profile  # Access profile created by signal
        for key, value in extra_fields.items():
            setattr(profile, key, value)
        profile.save()

        return user
