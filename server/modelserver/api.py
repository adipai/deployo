from azure.storage.queue import QueueService
from modelserver import app,queue_service
from flask import url_for, request, render_template, Response, jsonify, redirect

def deque_binary_message(qname):
'''
Retrieve message from front of the queue and deletes it
'''
    queue_service.decode_function = QueueMessageFormat.binary_base64decode
    message = queue_service.get_messages(qname)
    retrieved_message=message.content
    queue_service.delete_message(qname, message.id, message.pop_receipt)
    return retrieved_message

def deque_text_message(qname):
'''
Retrieve message from front of the queue and deletes it
'''
    message = queue_service.get_messages(qname)
    retrieved_message=message.content
    queue_service.delete_message(qname, message.id, message.pop_receipt)
    return retrieved_message

def preprocess_input(model_input):
'''
method to preprocess the input
'''
    # define custom preprocessing pipeline
    return preprocessed_input


@app.route('/api', methods=['GET'])
def run_model():
'''
pop from queue to serving model input
'''
    model_input = deque_text_message(qname)
    # model_input = deque_binary_message(qname)
    # preprocessed_input = preprocess_input(model_input)
    # model serving here


@app.route('/', methods=['GET'])
def home():
    return "api-root"
