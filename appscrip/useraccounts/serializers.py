# from rest_framework import serializers
# from .models import Users

# class RegistrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = [
#             "name",
#             "Email_Address",
#             "zipcode",
#             "Date_of_Birth",
#             "password",

#         ]

#         extra_kwargs = {"password": {"write_only": True}}
#         password = self.validated_data["password"]
#         user.set_password(password)
#         user.save()
#         return account