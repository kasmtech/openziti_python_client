# PostureResponseEndpointStateCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unlocked** | **bool** |  | [optional] 
**woken** | **bool** |  | [optional] 

## Example

```python
from openziti_edge_client.models.posture_response_endpoint_state_create import PostureResponseEndpointStateCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseEndpointStateCreate from a JSON string
posture_response_endpoint_state_create_instance = PostureResponseEndpointStateCreate.from_json(json)
# print the JSON string representation of the object
print(PostureResponseEndpointStateCreate.to_json())

# convert the object into a dict
posture_response_endpoint_state_create_dict = posture_response_endpoint_state_create_instance.to_dict()
# create an instance of PostureResponseEndpointStateCreate from a dict
posture_response_endpoint_state_create_from_dict = PostureResponseEndpointStateCreate.from_dict(posture_response_endpoint_state_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


