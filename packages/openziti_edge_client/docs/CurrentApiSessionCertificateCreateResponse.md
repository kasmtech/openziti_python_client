# CurrentApiSessionCertificateCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | [optional] 
**id** | **str** |  | [optional] 
**cas** | **str** |  | [optional] 
**certificate** | **str** |  | 

## Example

```python
from openziti_edge_client.models.current_api_session_certificate_create_response import CurrentApiSessionCertificateCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentApiSessionCertificateCreateResponse from a JSON string
current_api_session_certificate_create_response_instance = CurrentApiSessionCertificateCreateResponse.from_json(json)
# print the JSON string representation of the object
print(CurrentApiSessionCertificateCreateResponse.to_json())

# convert the object into a dict
current_api_session_certificate_create_response_dict = current_api_session_certificate_create_response_instance.to_dict()
# create an instance of CurrentApiSessionCertificateCreateResponse from a dict
current_api_session_certificate_create_response_from_dict = CurrentApiSessionCertificateCreateResponse.from_dict(current_api_session_certificate_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


