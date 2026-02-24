# openziti_edge_client.PostureChecksApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_posture_response**](PostureChecksApi.md#create_posture_response) | **POST** /posture-response | Submit a posture response to a posture query
[**create_posture_response_bulk**](PostureChecksApi.md#create_posture_response_bulk) | **POST** /posture-response-bulk | Submit multiple posture responses


# **create_posture_response**
> PostureResponseEnvelope create_posture_response(posture_response)

Submit a posture response to a posture query

Submits posture responses

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.posture_response_create import PostureResponseCreate
from openziti_edge_client.models.posture_response_envelope import PostureResponseEnvelope
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
    api_instance = openziti_edge_client.PostureChecksApi(api_client)
    posture_response = openziti_edge_client.PostureResponseCreate() # PostureResponseCreate | A Posture Response

    try:
        # Submit a posture response to a posture query
        api_response = api_instance.create_posture_response(posture_response)
        print("The response of PostureChecksApi->create_posture_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostureChecksApi->create_posture_response: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_response** | [**PostureResponseCreate**](PostureResponseCreate.md)| A Posture Response | 

### Return type

[**PostureResponseEnvelope**](PostureResponseEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contains a list of services that have had their timers altered |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_posture_response_bulk**
> PostureResponseEnvelope create_posture_response_bulk(posture_response)

Submit multiple posture responses

Submits posture responses

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.posture_response_create import PostureResponseCreate
from openziti_edge_client.models.posture_response_envelope import PostureResponseEnvelope
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
    api_instance = openziti_edge_client.PostureChecksApi(api_client)
    posture_response = [openziti_edge_client.PostureResponseCreate()] # List[PostureResponseCreate] | A Posture Response

    try:
        # Submit multiple posture responses
        api_response = api_instance.create_posture_response_bulk(posture_response)
        print("The response of PostureChecksApi->create_posture_response_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostureChecksApi->create_posture_response_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **posture_response** | [**List[PostureResponseCreate]**](PostureResponseCreate.md)| A Posture Response | 

### Return type

[**PostureResponseEnvelope**](PostureResponseEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contains a list of services that have had their timers altered |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

