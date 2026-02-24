# openziti_edge_client.EnrollApi

All URIs are relative to *https://demo.ziti.dev/edge/client/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enroll**](EnrollApi.md#enroll) | **POST** /enroll | Enroll an identity via one-time-token
[**enroll_ca**](EnrollApi.md#enroll_ca) | **POST** /enroll/ca | Enroll an identity with a pre-exchanged certificate
[**enroll_er_ott**](EnrollApi.md#enroll_er_ott) | **POST** /enroll/erott | Enroll an edge-router
[**enroll_ott**](EnrollApi.md#enroll_ott) | **POST** /enroll/ott | Enroll an identity via one-time-token
[**enroll_ott_ca**](EnrollApi.md#enroll_ott_ca) | **POST** /enroll/ottca | Enroll an identity via one-time-token with a pre-exchanged client certificate
[**enroll_token**](EnrollApi.md#enroll_token) | **POST** /enroll/token | 
[**enroll_updb**](EnrollApi.md#enroll_updb) | **POST** /enroll/updb | Enroll an identity via one-time-token
[**enrollment_challenge**](EnrollApi.md#enrollment_challenge) | **POST** /enroll/challenge | Allows verification of a controller or cluster of controllers as being the valid target for enrollment.
[**extend_current_identity_authenticator**](EnrollApi.md#extend_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend | Allows the current identity to recieve a new certificate associated with a certificate based authenticator
[**extend_router_enrollment**](EnrollApi.md#extend_router_enrollment) | **POST** /enroll/extend/router | Extend the life of a currently enrolled router&#39;s certificates
[**extend_verify_current_identity_authenticator**](EnrollApi.md#extend_verify_current_identity_authenticator) | **POST** /current-identity/authenticators/{id}/extend-verify | Allows the current identity to validate reciept of a new client certificate
[**get_enrollment_jwks**](EnrollApi.md#get_enrollment_jwks) | **GET** /enroll/jwks | List JSON Web Keys associated with enrollment


# **enroll**
> EnrollmentCertsEnvelope enroll(token=token, method=method, body=body)

Enroll an identity via one-time-token

present a OTT and CSR to receive a long-lived client certificate

### Example


```python
import openziti_edge_client
from openziti_edge_client.models.enrollment_certs_envelope import EnrollmentCertsEnvelope
from openziti_edge_client.models.generic_enroll import GenericEnroll
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    token = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)
    method = 'method_example' # str |  (optional)
    body = openziti_edge_client.GenericEnroll() # GenericEnroll |  (optional)

    try:
        # Enroll an identity via one-time-token
        api_response = api_instance.enroll(token=token, method=method, body=body)
        print("The response of EnrollApi->enroll:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **UUID**|  | [optional] 
 **method** | **str**|  | [optional] 
 **body** | [**GenericEnroll**](GenericEnroll.md)|  | [optional] 

### Return type

[**EnrollmentCertsEnvelope**](EnrollmentCertsEnvelope.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/pkcs7, application/json, application/x-pem-file, text/plain
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing and identities client certificate chains |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**409** | The request could not be completed due to a conflict of configuration or state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**410** | The request could not be completed as the resource is no longer available |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_ca**
> Empty enroll_ca()

Enroll an identity with a pre-exchanged certificate

For CA auto enrollment, an identity is not created beforehand.
Instead one will be created during enrollment. The client will present a client certificate that is signed by a
Certificate Authority that has been added and verified (See POST /cas and POST /cas/{id}/verify).

During this process no CSRs are requires as the client should already be in possession of a valid certificate.


### Example


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


# Enter a context with an instance of the API client
with openziti_edge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openziti_edge_client.EnrollApi(api_client)

    try:
        # Enroll an identity with a pre-exchanged certificate
        api_response = api_instance.enroll_ca()
        print("The response of EnrollApi->enroll_ca:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll_ca: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_er_ott**
> EnrollmentCertsEnvelope enroll_er_ott(er_ott_enrollment_request)

Enroll an edge-router

Enrolls an edge-router via a one-time-token to establish a certificate based identity.


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.enrollment_certs_envelope import EnrollmentCertsEnvelope
from openziti_edge_client.models.er_ott_enrollment_request import ErOttEnrollmentRequest
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    er_ott_enrollment_request = openziti_edge_client.ErOttEnrollmentRequest() # ErOttEnrollmentRequest | An OTT enrollment request

    try:
        # Enroll an edge-router
        api_response = api_instance.enroll_er_ott(er_ott_enrollment_request)
        print("The response of EnrollApi->enroll_er_ott:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll_er_ott: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **er_ott_enrollment_request** | [**ErOttEnrollmentRequest**](ErOttEnrollmentRequest.md)| An OTT enrollment request | 

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
**200** | A response containing the edge routers signed certificates (server chain, server cert, CAs). |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_ott**
> EnrollmentCertsEnvelope enroll_ott(ott_enrollment_request)

Enroll an identity via one-time-token

Enroll an identity via a one-time-token which is supplied via a query string parameter. This enrollment method
expects a PEM encoded CSRs to be provided for fulfillment. It is up to the enrolling identity to manage the
private key backing the CSR request.


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.enrollment_certs_envelope import EnrollmentCertsEnvelope
from openziti_edge_client.models.ott_enrollment_request import OttEnrollmentRequest
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    ott_enrollment_request = openziti_edge_client.OttEnrollmentRequest() # OttEnrollmentRequest | An OTT enrollment request

    try:
        # Enroll an identity via one-time-token
        api_response = api_instance.enroll_ott(ott_enrollment_request)
        print("The response of EnrollApi->enroll_ott:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll_ott: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ott_enrollment_request** | [**OttEnrollmentRequest**](OttEnrollmentRequest.md)| An OTT enrollment request | 

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
**200** | A response containing and identities client certificate chains |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_ott_ca**
> Empty enroll_ott_ca(ott_enrollment_request)

Enroll an identity via one-time-token with a pre-exchanged client certificate

Enroll an identity via a one-time-token that also requires a pre-exchanged client certificate to match a
Certificate Authority that has been added and verified (See POST /cas and POST /cas{id}/verify). The client
must present a client certificate signed by CA associated with the enrollment. This enrollment is similar to
CA auto enrollment except that is required the identity to be pre-created.

As the client certificate has been pre-exchanged there is no CSR input to this enrollment method.


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.empty import Empty
from openziti_edge_client.models.ott_enrollment_request import OttEnrollmentRequest
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    ott_enrollment_request = openziti_edge_client.OttEnrollmentRequest() # OttEnrollmentRequest | An OTT enrollment request

    try:
        # Enroll an identity via one-time-token with a pre-exchanged client certificate
        api_response = api_instance.enroll_ott_ca(ott_enrollment_request)
        print("The response of EnrollApi->enroll_ott_ca:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll_ott_ca: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ott_enrollment_request** | [**OttEnrollmentRequest**](OttEnrollmentRequest.md)| An OTT enrollment request | 

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_token**
> EnrollmentCertsEnvelope enroll_token(authorization, token_enrollment_request, ziti_token_issuer_id=ziti_token_issuer_id)

### Example


```python
import openziti_edge_client
from openziti_edge_client.models.enrollment_certs_envelope import EnrollmentCertsEnvelope
from openziti_edge_client.models.token_enrollment_request import TokenEnrollmentRequest
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    authorization = 'authorization_example' # str | An identifying token to enroll with
    token_enrollment_request = openziti_edge_client.TokenEnrollmentRequest() # TokenEnrollmentRequest | A  enrollment request with or without a CSR. Including a CSR indicated an attempt to enroll with certificate  credentials. If no CSR is included, the request is assumed to be a token enrollment request that will authenticate via tokens. 
    ziti_token_issuer_id = 'ziti_token_issuer_id_example' # str | The id of the token issuer to use for enrollment, optional as long the the token is not opaque (optional)

    try:
        api_response = api_instance.enroll_token(authorization, token_enrollment_request, ziti_token_issuer_id=ziti_token_issuer_id)
        print("The response of EnrollApi->enroll_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| An identifying token to enroll with | 
 **token_enrollment_request** | [**TokenEnrollmentRequest**](TokenEnrollmentRequest.md)| A  enrollment request with or without a CSR. Including a CSR indicated an attempt to enroll with certificate  credentials. If no CSR is included, the request is assumed to be a token enrollment request that will authenticate via tokens.  | 
 **ziti_token_issuer_id** | **str**| The id of the token issuer to use for enrollment, optional as long the the token is not opaque | [optional] 

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
**200** | A response containing and identities client certificate chains |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**409** | The request could not be completed due to a conflict of configuration or state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**410** | The request could not be completed as the resource is no longer available |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_updb**
> Empty enroll_updb(token, updb_credentials)

Enroll an identity via one-time-token

Enrolls an identity via a one-time-token to establish an initial username and password combination


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.empty import Empty
from openziti_edge_client.models.enroll_updb_request import EnrollUpdbRequest
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    token = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    updb_credentials = openziti_edge_client.EnrollUpdbRequest() # EnrollUpdbRequest | 

    try:
        # Enroll an identity via one-time-token
        api_response = api_instance.enroll_updb(token, updb_credentials)
        print("The response of EnrollApi->enroll_updb:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enroll_updb: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **UUID**|  | 
 **updb_credentials** | [**EnrollUpdbRequest**](EnrollUpdbRequest.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Base empty response |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**404** | The requested resource does not exist |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**503** | The request could not be completed due to the server being busy or in a temporarily bad state |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enrollment_challenge**
> NonceSignature enrollment_challenge(nonce)

Allows verification of a controller or cluster of controllers as being the valid target for enrollment.

A caller may submit a nonce and a key id (kid) from the enrollment JWKS endpoint or enrollment JWT that will
be used to sign the nonce. The resulting signature may be validated with the associated public key in order
to verify a networks identity during enrollment. The nonce must be a valid formatted UUID.


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.nonce_challenge import NonceChallenge
from openziti_edge_client.models.nonce_signature import NonceSignature
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    nonce = openziti_edge_client.NonceChallenge() # NonceChallenge | 

    try:
        # Allows verification of a controller or cluster of controllers as being the valid target for enrollment.
        api_response = api_instance.enrollment_challenge(nonce)
        print("The response of EnrollApi->enrollment_challenge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->enrollment_challenge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nonce** | [**NonceChallenge**](NonceChallenge.md)|  | 

### Return type

[**NonceSignature**](NonceSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A nonce challenge response. The contents will be the signature of the nonce, the key id used, and algorithm used to produce the signature. |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**400** | The supplied request contains invalid fields or could not be parsed (json and non-json bodies). The error&#39;s code, message, and cause fields can be inspected for further information |  * WWW-Authenticate - Denotes different type of security token related information <br>  |
**429** | The resource requested is rate limited and the rate limit has been exceeded |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    extend = openziti_edge_client.IdentityExtendEnrollmentRequest() # IdentityExtendEnrollmentRequest | 

    try:
        # Allows the current identity to recieve a new certificate associated with a certificate based authenticator
        api_response = api_instance.extend_current_identity_authenticator(id, extend)
        print("The response of EnrollApi->extend_current_identity_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->extend_current_identity_authenticator: %s\n" % e)
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    router_extend_enrollment_request = openziti_edge_client.RouterExtendEnrollmentRequest() # RouterExtendEnrollmentRequest | 

    try:
        # Extend the life of a currently enrolled router's certificates
        api_response = api_instance.extend_router_enrollment(router_extend_enrollment_request)
        print("The response of EnrollApi->extend_router_enrollment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->extend_router_enrollment: %s\n" % e)
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
    api_instance = openziti_edge_client.EnrollApi(api_client)
    id = 'id_example' # str | The id of the requested resource
    extend = openziti_edge_client.IdentityExtendValidateEnrollmentRequest() # IdentityExtendValidateEnrollmentRequest | 

    try:
        # Allows the current identity to validate reciept of a new client certificate
        api_response = api_instance.extend_verify_current_identity_authenticator(id, extend)
        print("The response of EnrollApi->extend_verify_current_identity_authenticator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->extend_verify_current_identity_authenticator: %s\n" % e)
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

# **get_enrollment_jwks**
> Jwks get_enrollment_jwks()

List JSON Web Keys associated with enrollment

Returns a list of JSON Web Keys (JWKS) that are used for enrollment signing. The keys listed here are used
to sign and co-sign enrollment JWTs. They can be verified through a challenge endpoint, using the public keys
from this endpoint to verify the target machine has possession of the related private key.


### Example


```python
import openziti_edge_client
from openziti_edge_client.models.jwks import Jwks
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
    api_instance = openziti_edge_client.EnrollApi(api_client)

    try:
        # List JSON Web Keys associated with enrollment
        api_response = api_instance.get_enrollment_jwks()
        print("The response of EnrollApi->get_enrollment_jwks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnrollApi->get_enrollment_jwks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Jwks**](Jwks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JWKS response for enrollment. |  * WWW-Authenticate - Denotes different type of security token related information <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

