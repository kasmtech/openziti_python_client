# PostureResponseProcessCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** |  | [optional] 
**is_running** | **bool** |  | [optional] 
**path** | **str** |  | [optional] 
**signer_fingerprints** | **List[str]** |  | [optional] 

## Example

```python
from openziti_edge_client.models.posture_response_process_create import PostureResponseProcessCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseProcessCreate from a JSON string
posture_response_process_create_instance = PostureResponseProcessCreate.from_json(json)
# print the JSON string representation of the object
print(PostureResponseProcessCreate.to_json())

# convert the object into a dict
posture_response_process_create_dict = posture_response_process_create_instance.to_dict()
# create an instance of PostureResponseProcessCreate from a dict
posture_response_process_create_from_dict = PostureResponseProcessCreate.from_dict(posture_response_process_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


