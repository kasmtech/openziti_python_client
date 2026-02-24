# EnrollUpdbRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_client.models.enroll_updb_request import EnrollUpdbRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollUpdbRequest from a JSON string
enroll_updb_request_instance = EnrollUpdbRequest.from_json(json)
# print the JSON string representation of the object
print(EnrollUpdbRequest.to_json())

# convert the object into a dict
enroll_updb_request_dict = enroll_updb_request_instance.to_dict()
# create an instance of EnrollUpdbRequest from a dict
enroll_updb_request_from_dict = EnrollUpdbRequest.from_dict(enroll_updb_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


