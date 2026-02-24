# PostureResponseService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**posture_query_type** | **str** |  | 
**timeout** | **int** |  | 
**timeout_remaining** | **int** |  | 

## Example

```python
from openziti_edge_client.models.posture_response_service import PostureResponseService

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseService from a JSON string
posture_response_service_instance = PostureResponseService.from_json(json)
# print the JSON string representation of the object
print(PostureResponseService.to_json())

# convert the object into a dict
posture_response_service_dict = posture_response_service_instance.to_dict()
# create an instance of PostureResponseService from a dict
posture_response_service_from_dict = PostureResponseService.from_dict(posture_response_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


