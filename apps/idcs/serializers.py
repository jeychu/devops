from rest_framework import serializers
from .models import Idc

class IdcSerializer(serializers.Serializer):
    """
    Idc serializer
    """
    id      = serializers.IntegerField(read_only=True)
    name    = serializers.CharField(required=True, max_length=32,
                                    label="Name",
                                    help_text="The name of the computer room")
    address = serializers.CharField(required=True, max_length=256,
                                    label="Address",
                                    help_text="The address of computer room")
    phone   = serializers.CharField(required=True, max_length=15,
                                    label="Phone",
                                    help_text="The phone number of the computer room")
    email   = serializers.EmailField(required=True, label="Email",
                                     help_text="Email address")
    letter  = serializers.CharField(required=True,max_length=5,
                                    label="Abbreviation",
                                    help_text="The abbr of the IDC",
                                    error_messages={"required": "Required",
                                                    "blank": "Not blank"})


    def create(self, validated_data):
        return Idc.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.address = validated_data.get("address", instance.address)
        instance.phone = validated_data.get("phone",instance.phone)
        instance.email = validated_data.get("email",instance.email)
        instance.save()
        return instance




