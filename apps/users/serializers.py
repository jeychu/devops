from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    """
    user serializer
    """
    id          = serializers.CharField()
    username    = serializers.CharField()
    email       = serializers.EmailField()