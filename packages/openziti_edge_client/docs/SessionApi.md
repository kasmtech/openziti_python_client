# openziti_edge_client.SessionApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](SessionApi.md#create_session) | **POST** /sessions | Create a session resource
[**delete_session**](SessionApi.md#delete_session) | **DELETE** /sessions/{id} | Delete a session
[**detail_session**](SessionApi.md#detail_session) | **GET** /sessions/{id} | Retrieves a single session
[**list_sessions**](SessionApi.md#list_sessions) | **GET** /sessions | List sessions


# **create_session**
> SessionCreateEnvelope create_session(session)

Create a session resource

Create a session resource.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.session_create import SessionCreate
from openziti_edge_client.models.session_create_envelope import SessionCreateEnvelope
from openziti_edge_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_client.SessionApi(api_client)
    session = openziti_edge_client.SessionCreate() # SessionCreate | A session to create

    try:
        # Create a session resource
        api_response = api_instance.create_session(session)
        print("The response of SessionApi->create_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->create_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session** | [**SessionCreate**](SessionCreate.md)| A session to create | 

### Return type

[**SessionCreateEnvelope**](SessionCreateEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The create request was successful and the resource has been added at the following location |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_session**
> Empty delete_session(id)

Delete a session

Delete a session by id.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.empty import Empty
from openziti_edge_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_client.SessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Delete a session
        api_response = api_instance.delete_session(id)
        print("The response of SessionApi->delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->delete_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The delete request was successful and the resource has been removed |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**409** | The resource requested to be removed/altered cannot be as it is referenced by another object. |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detail_session**
> DetailSessionEnvelope detail_session(id)

Retrieves a single session

Retrieves a single session by id.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.detail_session_envelope import DetailSessionEnvelope
from openziti_edge_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_client.SessionApi(api_client)
    id = 'id_example' # str | The id of the requested resource

    try:
        # Retrieves a single session
        api_response = api_instance.detail_session(id)
        print("The response of SessionApi->detail_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->detail_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 

### Return type

[**DetailSessionEnvelope**](DetailSessionEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single session |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions**
> ListSessionsEnvelope list_sessions(limit=limit, offset=offset, filter=filter)

List sessions

Retrieves a list of active sessions resources; supports filtering, sorting, and pagination.

Sessions are tied to an API session and are moved when an API session times out or logs out. Active sessions
(i.e. Ziti SDK connected to an edge router) will keep the session and API session marked as active.


### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.list_sessions_envelope import ListSessionsEnvelope
from openziti_edge_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ztSession
configuration.api_key['ztSession'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ztSession'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_client.SessionApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List sessions
        api_response = api_instance.list_sessions(limit=limit, offset=offset, filter=filter)
        print("The response of SessionApi->list_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SessionApi->list_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListSessionsEnvelope**](ListSessionsEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sessions |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

