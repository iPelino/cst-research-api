from .models import *
from rest_framework import serializers


class THLIC_CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = THLIC_Certificate
        fields = '__all__'

class Teaching_portofolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teaching_portofolio
        fields = '__all__'