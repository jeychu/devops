from rest_framework import serializers
from .models import Manufacturer, ProductModel

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

    def validate_model_name(self, value):
        print(value.upper())
        return value.upper()

    def validate(self, attrs):
        #print(attrs)
        manufacturer_obj = attrs["vendor"]
        try:
            if manufacturer_obj.productmodel_set.get(model_name__exact=attrs["model_name"]):
                raise serializers.ValidationError("The model exists")
        except ProductModel.DoesNotExist:
            print(attrs)
            return attrs


    def to_representation(self, instance):
        vendor = instance.vendor
        ret = super(ProductModelSerializer, self).to_representation(instance)
        ret["vendor"] = {
            "id": vendor.id,
            "name":vendor.vendor_name
        }
        return ret

