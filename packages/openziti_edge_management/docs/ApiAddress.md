# ApiAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openziti_edge_management.models.api_address import ApiAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAddress from a JSON string
api_address_instance = ApiAddress.from_json(json)
# print the JSON string representation of the object
print(ApiAddress.to_json())

# convert the object into a dict
api_address_dict = api_address_instance.to_dict()
# create an instance of ApiAddress from a dict
api_address_from_dict = ApiAddress.from_dict(api_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


