from django.core.management.base import BaseCommand

from erp_receiver.utils import MessageReciever
from erp_receiver.utils.db import save_upload_data_from_str
from market_place.settings import QUEUE_NAME


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):

        with MessageReciever() as receiver:
            receiver.consume_messages(queue=QUEUE_NAME, callback=save_upload_data_from_str)  # передать коллбек, который будет
            # отрабатывать, когда получит значения из очереди

