# openziti_edge_client.ExternalJWTSignerApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_external_jwt_signers**](ExternalJWTSignerApi.md#list_external_jwt_signers) | **GET** /external-jwt-signers | List Client Authentication External JWT


# **list_external_jwt_signers**
> ListClientExternalJwtSignersEnvelope list_external_jwt_signers(limit=limit, offset=offset, filter=filter)

List Client Authentication External JWT

Retrieves a list of external JWT signers for authentication

### Example


```python
import openziti_edge_client
from openziti_edge_client.models.list_client_external_jwt_signers_envelope import ListClientExternalJwtSignersEnvelope
from openziti_edge_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.ziti.dev/edge/client/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openziti_edge_client.Configuration(
    host = "https://demo.ziti.dev/edge/client/v1"
)


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_client.ExternalJWTSignerApi(api_client)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    filter = 'filter_example' # str |  (optional)

    try:
        # List Client Authentication External JWT
        api_response = api_instance.list_external_jwt_signers(limit=limit, offset=offset, filter=filter)
        print("The response of ExternalJWTSignerApi->list_external_jwt_signers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalJWTSignerApi->list_external_jwt_signers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **filter** | **str**|  | [optional] 

### Return type

[**ListClientExternalJwtSignersEnvelope**](ListClientExternalJwtSignersEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of External JWT Signers |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

