from rest_framework import serializers

from .models import Name, Cricketer, Color


class NameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Name
		fields = "__all__"


class CricketerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cricketer
		fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Color
		fields = "__all__"
