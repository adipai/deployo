from azure.storage.queue import QueueService

acc_name='<storage-account-name-here>'
key = '<unique-key-here>'

queue_service = QueueService(account_name=acc_name, account_key=key)

def create_new_queue(qname):
'''
Create a new queue in the storage account
'''
    queue_service.create_queue(qname)


def peek_into_queue(qname,n):
'''
Retrieves n<32 messages from the front of the queue, but does not alter the visibility of the message.
'''
    messages = queue_service.peek_messages(qname,num_messages=n)
    for message in messages:
        print(message.content)

def clear_queue(qname):
'''
Clears the entire queue
'''
    queue_service.clear_messages(qname)

def del_queue(qname):
'''
Deletes an existing queue
'''
    queue_service.delete_queue(qname)
