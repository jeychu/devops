from rest_framework import serializers
from idcs.serializers import IdcSerializer
from .models import Cabinet
from idcs.models import Idc

class CabinetSerializer(serializers.Serializer):
    # The second step of deserialization: validate the field
    idc     = serializers.PrimaryKeyRelatedField(many=False, queryset=Idc.objects.all())
    name    = serializers.CharField(required=True)

   #def get_idc(self, obj):
   #     print(obj)
   #     print(obj.idc)
   #     return {
   #         "id": obj.id,
   #         "name": obj.name
   #     }


    # The last step of the serialization to Json
    # When the data not in the database, but needed by the user
    # manipulated here
    def to_representation(self, instance):
        idc_obj = instance.idc
        print(instance.idc)
        ret = super(CabinetSerializer, self).to_representation(instance)
        ret["idc"] = {
            "id": idc_obj.id,
            "name": idc_obj.name
        }

        return ret

    def to_internal_value(self, data):
        """
        The firste step of Deserialization's :
        receives the raw data(QueryDict <=> request.GET, request.POST),
        then map the raw data to serializd fields.
        When the data not from the user but from ourselves, manipulated
        here.
        :param data:
        :return:
        """
        print(data)
        return super(CabinetSerializer, self).to_internal_value(data)

    # The third step of deserialization: create the entry to the database
    def create(self, validated_data):
        raise serializers.ValidationError("create error")
        return Cabinet.objects.create(**validated_data)



