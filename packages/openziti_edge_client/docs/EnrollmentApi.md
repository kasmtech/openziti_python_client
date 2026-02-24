# openziti_edge_client.EnrollmentApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_network_jwts**](EnrollmentApi.md#list_network_jwts) | **GET** /network-jwts | Returns a list of JWTs suitable for bootstrapping network trust.


# **list_network_jwts**
> ListNetworkJWTsEnvelope list_network_jwts()

Returns a list of JWTs suitable for bootstrapping network trust.

Returns a list of JWTs for trusting a network

### Example


```python
import openziti_edge_client
from openziti_edge_client.models.list_network_jwts_envelope import ListNetworkJWTsEnvelope
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
    api_instance = openziti_edge_client.EnrollmentApi(api_client)

    try:
        # Returns a list of JWTs suitable for bootstrapping network trust.
        api_response = api_instance.list_network_jwts()
        print("The response of EnrollmentApi->list_network_jwts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollmentApi->list_network_jwts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListNetworkJWTsEnvelope**](ListNetworkJWTsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of network JWTs |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

