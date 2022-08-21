import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from erp_receiver.utils import MessageReciever
from erp_receiver.utils.db import save_upload_data_from_dict
from market_place.settings import QUEUE_NAME


@api_view(['POST'])
def hello_world(request):
    data = request.data
    save_upload_data_from_dict(data)
    return Response({"message": "Success"})


class DownloadData(APIView):
    def post(self, request, *args, **kwargs):
        queue_name = QUEUE_NAME

        with MessageReciever() as receiver:
            receiver.consume_messages(queue=queue_name, callback=None)  # передать коллбек, который будет отрабатывать, когда получит значения из очереди
