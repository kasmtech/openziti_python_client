# ErOttEnrollmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_csr** | **str** |  | [optional] 
**server_csr** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openziti_edge_client.models.er_ott_enrollment_request import ErOttEnrollmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ErOttEnrollmentRequest from a JSON string
er_ott_enrollment_request_instance = ErOttEnrollmentRequest.from_json(json)
# print the JSON string representation of the object
print(ErOttEnrollmentRequest.to_json())

# convert the object into a dict
er_ott_enrollment_request_dict = er_ott_enrollment_request_instance.to_dict()
# create an instance of ErOttEnrollmentRequest from a dict
er_ott_enrollment_request_from_dict = ErOttEnrollmentRequest.from_dict(er_ott_enrollment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


