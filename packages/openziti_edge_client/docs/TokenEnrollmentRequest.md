# TokenEnrollmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_csr** | **str** |  | [optional] 

## Example

```python
from openziti_edge_client.models.token_enrollment_request import TokenEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenEnrollmentRequest from a JSON string
token_enrollment_request_instance = TokenEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(TokenEnrollmentRequest.to_json())

# convert the object into a dict
token_enrollment_request_dict = token_enrollment_request_instance.to_dict()
# create an instance of TokenEnrollmentRequest from a dict
token_enrollment_request_from_dict = TokenEnrollmentRequest.from_dict(token_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


