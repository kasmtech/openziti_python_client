# GenericEnroll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_csr** | **str** |  | [optional] 
**client_csr** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**server_cert_csr** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_client.models.generic_enroll import GenericEnroll

# TODO update the JSON string below
json = "{}"
# create an instance of GenericEnroll from a JSON string
generic_enroll_instance = GenericEnroll.from_json(json)
# print the JSON string representation of the object
print(GenericEnroll.to_json())

# convert the object into a dict
generic_enroll_dict = generic_enroll_instance.to_dict()
# create an instance of GenericEnroll from a dict
generic_enroll_from_dict = GenericEnroll.from_dict(generic_enroll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


