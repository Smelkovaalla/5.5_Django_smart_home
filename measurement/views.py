from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Temp_sensor, Temp_measure
from measurement.serializers import Temp_measureSerializer, Temp_sensorSerializer



class TemperatureView(APIView):
    def get(self, request):
        temperatures = Temp_measure.objects.all()
        temper = Temp_measureSerializer(temperatures, many=True)
        return Response(temper.data)

    def post(self, request):
        temp = Temp_measureSerializer(data=request.data)
        if temp.is_valid():
            if request.data.get('id'):
                ids = request.data.get(id)
                temp.save(id=ids)
            else:
                temp.save()
        return Response({'status': 'OK'})


class SensorsView(APIView):
    def get(self, request):
        temp_sensors = Temp_sensor.objects.all()
        sens = Temp_sensorSerializer(temp_sensors, many=True)
        return Response(sens.data)

    def post(self, request):
        sens = Temp_sensorSerializer(data=request.data)
        if sens.is_valid():
            if request.data.get('id'):
                ids = request.data.get(id)
                sens.save(id=ids)
            else:
                sens.save()
        return Response({'status': 'OK'})
