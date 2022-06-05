from rest_framework import serializers
from .models import DriverRegistrations, Customer, City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'



class DriverRegistrationSerializer(serializers.ModelSerializer):
    # city = serializers.PrimaryKeyRelatedField(many=True, required=True, queryset=City.objects.all())

    class Meta:
        model = DriverRegistrations
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['city'] = CitySerializer(instance.city).data.get('city')
        return response


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'