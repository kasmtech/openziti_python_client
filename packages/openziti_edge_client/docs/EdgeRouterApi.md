# openziti_edge_client.EdgeRouterApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_identity_edge_routers**](EdgeRouterApi.md#get_current_identity_edge_routers) | **GET** /current-identity/edge-routers | Return this list of Edge Routers the identity has access to


# **get_current_identity_edge_routers**
> ListCurrentIdentityEdgeRoutersEnvelope get_current_identity_edge_routers()

Return this list of Edge Routers the identity has access to

Lists the Edge Routers that the current identity has access to via policies. The data returned
includes their address and online status


### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.list_current_identity_edge_routers_envelope import ListCurrentIdentityEdgeRoutersEnvelope
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
    api_instance = openziti_edge_client.EdgeRouterApi(api_client)

    try:
        # Return this list of Edge Routers the identity has access to
        api_response = api_instance.get_current_identity_edge_routers()
        print("The response of EdgeRouterApi->get_current_identity_edge_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeRouterApi->get_current_identity_edge_routers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListCurrentIdentityEdgeRoutersEnvelope**](ListCurrentIdentityEdgeRoutersEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of edge routers |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

