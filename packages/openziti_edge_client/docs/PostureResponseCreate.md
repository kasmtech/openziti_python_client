# PostureResponseCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type_id** | [**PostureCheckType**](PostureCheckType.md) |  | 

## Example

```python
from openziti_edge_client.models.posture_response_create import PostureResponseCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseCreate from a JSON string
posture_response_create_instance = PostureResponseCreate.from_json(json)
# print the JSON string representation of the object
print(PostureResponseCreate.to_json())

# convert the object into a dict
posture_response_create_dict = posture_response_create_instance.to_dict()
# create an instance of PostureResponseCreate from a dict
posture_response_create_from_dict = PostureResponseCreate.from_dict(posture_response_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


