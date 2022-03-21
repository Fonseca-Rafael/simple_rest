from unittest import TestCase
from starlette.testclient import TestClient
import json
from simple_rest import app

# sanity check

class TestSimpleRest(TestCase):
    def test(self):
        
        client = TestClient(app)
        
        response = client.get("/?item=bar")
        assert 'foo' == response.json()['bar'];
        
        response = client.get("/?item=baz")
        assert 'bee' == response.json()['baz'];
        
        response = client.get("/?item=bee")
        assert 'baz' == response.json()['bee'];
        
        response = client.get("/?item=foo")
        assert 'bar' == response.json()['foo'];
        
        response = client.get("/")
        assert 'Not Found' == response.json()['undefined']
        
