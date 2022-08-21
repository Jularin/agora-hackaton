from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.parser import Context
from api.rabbitmq import MessageConsumer
from api.services import get_file_extension, get_strategy_context
from api.models import User

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class UploadData(APIView):
    def post(self, request, *args, **kwargs):
        try:
            file: InMemoryUploadedFile = request.FILES['file']  # файл посылается через form-data с ключем file
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        raw_data = file.read().decode()  # строки файла

        queue_name: str = request.user.queue_name

        file_extension = get_file_extension(file.name)
        try:
            context: Context = get_strategy_context(file_extension)
        except KeyError:
            return Response(status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        data: dict = context.parse(raw_data)

        with MessageConsumer() as consumer:
            consumer.declare_queue(queue_name)
            try:
                consumer.send_message(exchange="", routing_key=queue_name, body=f"{data}")
            except Exception as e:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)  # или пикните другую ошибку

        return Response(status=status.HTTP_200_OK)
