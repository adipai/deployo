from azure.storage.queue import QueueService

acc_name='<storage-account-name-here>'
key = '<unique-key-here>'

queue_service = QueueService(account_name=acc_name,
                account_key=key)

def enqueue_text__input(message):
'''
The textual 'message' to be inserted into the queue from client side is sent to the queue with name 'qname'
'''
    queue_service.put_message(qname, message)

def enqueue_binary__input(message):
'''
The binary 'message' to be inserted into the queue from client side is sent to the queue with name 'qname',
can be used for sending images etc.
'''
    queue_service.encode_function = QueueMessageFormat.binary_base64encode
    queue_service.put_message(qname, message)
