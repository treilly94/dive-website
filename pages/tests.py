"""
This Module contains the tests
"""
from django.test.utils import setup_test_environment
from django.test import Client

setup_test_environment()
client = Client()

response = client.get('/')
