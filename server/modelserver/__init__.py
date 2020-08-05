from flask import Flask

acc_name='<storage-account-name-here>'
key = '<unique-key-here>'
queue_service = QueueService(account_name=acc_name,
                account_key=key)


app = Flask(__name__)
import modelserver.api
