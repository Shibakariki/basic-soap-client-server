# --- Importing the libraries for services ---

import requests
import random
from spyne.decorator import srpc
from spyne.service import ServiceBase
from models import Todos
from spyne.model.complex import Iterable
from spyne.model.primitive import String, Integer

# --- Importing the libraries for application and server ---

from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# --- Setup test url ---

url_test = "https://gorest.co.in/public/v2/todos"

# --- Defining the service ---

class TestService(ServiceBase):
    @srpc(_returns=Iterable(Iterable(Todos)))
    def test_request():
        response = requests.get(url_test)
        json_response = response.json()
        todos = []
        for json_data in json_response:
            todo = Todos(json_data)
            todos.append(todo)
        yield todos

class TestService2(ServiceBase):
    @srpc(_returns=Iterable(String))
    def test_request2():
        yield "Easier test"
        
    @srpc(Integer,String,_returns=Iterable(String))
    def random_from(rand,name):
        randnum = random.randint(0,rand)
        yield "<--- \nYou got {}, {}\n<---".format(randnum,name)

# --- Defining the server ---

app = Application([TestService,TestService2], 'spyne.test.http',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )
wsgi_app = WsgiApplication(app)

# --- Running the server ---
# --- The server will be running on http://localhost:7789 or on http://127.0.0.1:7789 ---

server = make_server('127.0.0.1', 7789, wsgi_app)

print ("listening to http://127.0.0.1:7789")
print ("wsdl is at: http://localhost:7789/?wsdl")

server.serve_forever()
