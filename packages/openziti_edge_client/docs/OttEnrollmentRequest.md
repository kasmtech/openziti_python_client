# OttEnrollmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_csr** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openziti_edge_client.models.ott_enrollment_request import OttEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OttEnrollmentRequest from a JSON string
ott_enrollment_request_instance = OttEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(OttEnrollmentRequest.to_json())

# convert the object into a dict
ott_enrollment_request_dict = ott_enrollment_request_instance.to_dict()
# create an instance of OttEnrollmentRequest from a dict
ott_enrollment_request_from_dict = OttEnrollmentRequest.from_dict(ott_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


