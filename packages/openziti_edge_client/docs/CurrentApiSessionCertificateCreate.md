# CurrentApiSessionCertificateCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csr** | **str** |  | 

## Example

```python
from openziti_edge_client.models.current_api_session_certificate_create import CurrentApiSessionCertificateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentApiSessionCertificateCreate from a JSON string
current_api_session_certificate_create_instance = CurrentApiSessionCertificateCreate.from_json(json)
# print the JSON string representation of the object
print(CurrentApiSessionCertificateCreate.to_json())

# convert the object into a dict
current_api_session_certificate_create_dict = current_api_session_certificate_create_instance.to_dict()
# create an instance of CurrentApiSessionCertificateCreate from a dict
current_api_session_certificate_create_from_dict = CurrentApiSessionCertificateCreate.from_dict(current_api_session_certificate_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


