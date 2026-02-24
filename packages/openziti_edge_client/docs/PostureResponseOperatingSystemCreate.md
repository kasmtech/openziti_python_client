# PostureResponseOperatingSystemCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | **str** |  | [optional] 
**type** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from openziti_edge_client.models.posture_response_operating_system_create import PostureResponseOperatingSystemCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseOperatingSystemCreate from a JSON string
posture_response_operating_system_create_instance = PostureResponseOperatingSystemCreate.from_json(json)
# print the JSON string representation of the object
print(PostureResponseOperatingSystemCreate.to_json())

# convert the object into a dict
posture_response_operating_system_create_dict = posture_response_operating_system_create_instance.to_dict()
# create an instance of PostureResponseOperatingSystemCreate from a dict
posture_response_operating_system_create_from_dict = PostureResponseOperatingSystemCreate.from_dict(posture_response_operating_system_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


