from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.dateparse import parse_datetime, parse_date
from core.models import Incident
from core.serializers import IncidentInputSerializer, IncidentSerializer


class IncidentAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = IncidentSerializer
    input_serializer_class = IncidentInputSerializer

    def get(self, request):
        cve_number = request.GET.get("cve_number")
        if cve_number:
            serializer = self.serializer_class(Incident.objects.filter(cve_number=cve_number), many=True)
        else:
            serializer = self.serializer_class(Incident.objects.all(), many=True)
        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.input_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Incident.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        serializer = self.input_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        Incident.objects.filter(pk=pk).update(**serializer.validated_data)
        return Response(status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk):
        incident = Incident.objects.filter(pk=pk)
        if not incident.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={"detail": "incident with this id does not exist"})
        incident.first().delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)


class IncidentByDateAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = IncidentSerializer

    def get(self, request):
        start_date, end_date = parse_datetime(request.GET.get("start_date")),\
                               parse_datetime(request.GET.get("end_date"))
        if not (start_date or end_date):
            return Response(
                data={"detail": "start date and end date were not provided"},
                status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(
            Incident.objects.filter(time_creation__gte=start_date, time_creation__lt=end_date), many=True)

        return Response(data=serializer.data,
                        status=status.HTTP_200_OK)
