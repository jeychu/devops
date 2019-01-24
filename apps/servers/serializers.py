from rest_framework import serializers
from manufacturer.models import Manufacturer, ProductModel
from .models import Server, NetworkDevice, IP

class ServerAutoReportSerializer(serializers.Serializer):
    """
    server auto-synchronization serialization
    """
    ip          = serializers.IPAddressField(required=True)
    hostname    = serializers.CharField(required=True, max_length=20)
    cpu         = serializers.CharField(required=True, max_length=50)
    mem         = serializers.CharField(required=True, max_length=20)
    disk        = serializers.CharField(required=True, max_length=200)
    os          = serializers.CharField(required=True, max_length=50)
    sn          = serializers.CharField(required=True, max_length=50)
    manufacturer= serializers.CharField(required=True)
    model_name  = serializers.CharField(required=True)
    uuid        = serializers.CharField(required=True, max_length=50)
    network     = serializers.JSONField(required=True)

    def validate_manufacturer(self, value):
        try:
            return Manufacturer.objects.get(vendor_name__exact=value)
        except Manufacturer.DoesNotExist:
            return self.create_manufacturer(value)

    def validate(self, attrs):
        manufacturer_obj = attrs["manufacturer"]
        try:
            attrs["model_name"] = manufacturer_obj.productmodel_set.get(model_name__exact=attrs["model_name"])
        except ProductModel.DoesNotExist:
            attrs["model_name"] = self.create_product_model(manufacturer_obj, attrs["model_name"])
        return attrs

    def create(self, validated_data):
        network = validated_data.pop("network")
        server_obj = Server.objects.create(**validated_data)
        self.check_server_network_device(server_obj, network)
        return server_obj

    def check_server_network_device(self, server_obj, network):
        """
        Check whether the specified server has these NIC devices or not
        then connect these two
        :return:
        """
        network_device_query = server_obj.networkdevice_set.all()
        for device in network:
            pass


    def create_manufacturer(self, vendor_name):
        return Manufacturer.objects.create(vendor_name=vendor_name)

    def create_product_model(self, manufacturer_obj, model_name):
        return ProductModel.objects.create(model_name=model_name,vendor=manufacturer_obj)

    def to_representation(self, instance):
        ret = {
            "hostname": instance.hostname,
            "ip": instance.ip
        }
        return ret

class ServerSerializer(serializers.ModelSerializer):
    """
    server serializer
    """
    class Meta:
        model = Server
        fields = "__all__"


class NetworkDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkDevice
        fields = "__all__"

class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IP
        fields = "__all__"
