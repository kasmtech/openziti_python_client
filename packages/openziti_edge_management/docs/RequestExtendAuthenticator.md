# RequestExtendAuthenticator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roll_keys** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_management.models.request_extend_authenticator import RequestExtendAuthenticator

# TODO update the JSON string below
json = "{}"
# create an instance of RequestExtendAuthenticator from a JSON string
request_extend_authenticator_instance = RequestExtendAuthenticator.from_json(json)
# print the JSON string representation of the object
print(RequestExtendAuthenticator.to_json())

# convert the object into a dict
request_extend_authenticator_dict = request_extend_authenticator_instance.to_dict()
# create an instance of RequestExtendAuthenticator from a dict
request_extend_authenticator_from_dict = RequestExtendAuthenticator.from_dict(request_extend_authenticator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


