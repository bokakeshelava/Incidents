from rest_framework import serializers

from core.models import Incident, IncidentName


class IncidentInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    cve_number = serializers.CharField()
    object = serializers.CharField()

    def validate(self, attrs):
        incident_name = IncidentName.objects.filter(name=attrs["name"])
        if not incident_name.exists():
            raise serializers.ValidationError("incident with this name does not exist")
        attrs["name"] = incident_name.first()

        return attrs


class IncidentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Incident
        fields = ('id', 'name', 'description', 'cve_number', 'object')
