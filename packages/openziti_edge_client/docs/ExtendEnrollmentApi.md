# openziti_edge_client.ExtendEnrollmentApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extend_current_identity_authenticator**](ExtendEnrollmentApi.md#extend_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend | Allows the current identity to recieve a new certificate associated with a certificate based authenticator
[**extend_router_enrollment**](ExtendEnrollmentApi.md#extend_router_enrollment) | **POST** /enroll/extend/router | Extend the life of a currently enrolled router&#39;s certificates
[**extend_verify_current_identity_authenticator**](ExtendEnrollmentApi.md#extend_verify_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend-verify | Allows the current identity to validate reciept of a new client certificate


# **extend_current_identity_authenticator**
> IdentityExtendEnrollmentEnvelope extend_current_identity_authenticator(id, extend)

Allows the current identity to recieve a new certificate associated with a certificate based authenticator

This endpoint only functions for certificates issued by the controller. 3rd party certificates are not handled.
Allows an identity to extend its certificate's expiration date by using its current and valid client certificate to submit a CSR. This CSR may be passed in using a new private key, thus allowing private key rotation.
The response from this endpoint is a new client certificate which the client must  be verified via the /authenticators/{id}/extend-verify endpoint.
After verification is completion any new connections must be made with new certificate. Prior to verification the old client certificate remains active.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.identity_extend_enrollment_envelope import IdentityExtendEnrollmentEnvelope
from openziti_edge_client.models.identity_extend_enrollment_request import IdentityExtendEnrollmentRequest
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
    api_instance = openziti_edge_client.ExtendEnrollmentApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    extend = openziti_edge_client.IdentityExtendEnrollmentRequest() # IdentityExtendEnrollmentRequest | 

    try:
        # Allows the current identity to recieve a new certificate associated with a certificate based authenticator
        api_response = api_instance.extend_current_identity_authenticator(id, extend)
        print("The response of ExtendEnrollmentApi->extend_current_identity_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtendEnrollmentApi->extend_current_identity_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **extend** | [**IdentityExtendEnrollmentRequest**](IdentityExtendEnrollmentRequest.md)|  | 

### Return type

[**IdentityExtendEnrollmentEnvelope**](IdentityExtendEnrollmentEnvelope.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containg the identity&#39;s new certificate |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_router_enrollment**
> EnrollmentCertsEnvelope extend_router_enrollment(router_extend_enrollment_request)

Extend the life of a currently enrolled router's certificates

Allows a router to extend its certificates' expiration date by
using its current and valid client certificate to submit a CSR. This CSR may
be passed in using a new private key, thus allowing private key rotation or swapping.

After completion any new connections must be made with certificates returned from a 200 OK
response. The previous client certificate is rendered invalid for use with the controller even if it
has not expired.

This request must be made using the existing, valid, client certificate.


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.enrollment_certs_envelope import EnrollmentCertsEnvelope
from openziti_edge_client.models.router_extend_enrollment_request import RouterExtendEnrollmentRequest
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
    api_instance = openziti_edge_client.ExtendEnrollmentApi(api_client)
    router_extend_enrollment_request = openziti_edge_client.RouterExtendEnrollmentRequest() # RouterExtendEnrollmentRequest | 

    try:
        # Extend the life of a currently enrolled router's certificates
        api_response = api_instance.extend_router_enrollment(router_extend_enrollment_request)
        print("The response of ExtendEnrollmentApi->extend_router_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtendEnrollmentApi->extend_router_enrollment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_extend_enrollment_request** | [**RouterExtendEnrollmentRequest**](RouterExtendEnrollmentRequest.md)|  | 

### Return type

[**EnrollmentCertsEnvelope**](EnrollmentCertsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing the edge routers new signed certificates (server chain, server cert, CAs). |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_verify_current_identity_authenticator**
> Empty extend_verify_current_identity_authenticator(id, extend)

Allows the current identity to validate reciept of a new client certificate

After submitting a CSR for a new client certificate the resulting public certificate must be re-submitted to this endpoint to verify receipt.
After receipt, the new client certificate must be used for new authentication requests.

### Example

* Api Key Authentication (ztSession):
* OAuth Authentication (oauth2):

```python
import openziti_edge_client
from openziti_edge_client.models.empty import Empty
from openziti_edge_client.models.identity_extend_validate_enrollment_request import IdentityExtendValidateEnrollmentRequest
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
    api_instance = openziti_edge_client.ExtendEnrollmentApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    extend = openziti_edge_client.IdentityExtendValidateEnrollmentRequest() # IdentityExtendValidateEnrollmentRequest | 

    try:
        # Allows the current identity to validate reciept of a new client certificate
        api_response = api_instance.extend_verify_current_identity_authenticator(id, extend)
        print("The response of ExtendEnrollmentApi->extend_verify_current_identity_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExtendEnrollmentApi->extend_verify_current_identity_authenticator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the requested resource | 
 **extend** | [**IdentityExtendValidateEnrollmentRequest**](IdentityExtendValidateEnrollmentRequest.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[ztSession](../README.md#ztSession), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**401** | The supplied session does not have the correct access rights to request this resource |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

