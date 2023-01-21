# basic-soap-client-server
A basic python soap client and server to get it started and configured quickly

## Environment Setup
> Note: This is a python 3 project

### Create a virtual environment
```bash
python -m venv c:\path\to\myenv
```
> Pour Linux/MacOS :
```bash	
source /path/to/myenv/bin/activate
```
> Pour Windows :
```bash
\path\to\myenv\Scripts\activate.bat
```
### Install dependencies
```bash
pip install -r requirements.txt
```
## Server Setup

### Create a service
```py
class Service1(ServiceBase):
    @srpc(_returns=Iterable(Type))
    def service1():
        [...]
        yield [...]
```
The service must inherit from `ServiceBase` and must have a `@srpc` decorator.
In this decorator, you must specify the return type of the service. And if you want to add parameters, you must specify them in the decorator.

Like this :
```py
@srpc(Integer,String,_returns=Iterable(String))
    def other_service(int,string):
        [...]
        yield [...]
```

### Create and launch the spyne based server
#### Create the server
```py
app = Application([Service1,...], 'spyne.services.http',
        in_protocol=Soap11(validator='lxml'),
        out_protocol=Soap11(),
    )
wsgi_app = WsgiApplication(app)
```	
#### Launch the server
```py
server = make_server('127.0.0.1', 7789, wsgi_app)

print ("listening to http://127.0.0.1:7789")
print ("wsdl is at: http://localhost:7789/?wsdl")

server.serve_forever()
```
When the server is launched, you can access to the wsdl at the address `http://localhost:7789/?wsdl`, and you can test the services with a soap client.
> Note: If the port 7789 is already used, you can change it.

## Client Setup
In this example, we will use the `suds` and `zeep` library to create a client.
### Create the zeep client
```py
client = zeep.Client('http://localhost:7789/?wsdl')
```
### Create the suds client
```py
client = suds.client.Client('http://localhost:7789/?wsdl')
```
### Call a service
```py
client.service.service1()
```
> Note : The name of the service is the name of the function in the class.

> Note : If you have parameters, you must specify them in the function call.

> Note : Data management is different between the two clients. For more information, you can check the documentation of the library.

## Documentation
- [Spyne](https://spyne.io/)
- [Suds-jurko](https://pypi.org/project/suds-jurko/) ([Suds](https://fedorahosted.org/suds/))
- [Zeep](https://python-zeep.readthedocs.io/en/master/)

## Example
You can find an example in the `example` folder.
These examples are some essential services to get started with a soap client and server.
If you want to do more complex services, you can check the documentation of the libraries.