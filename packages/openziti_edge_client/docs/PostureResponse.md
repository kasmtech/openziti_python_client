# PostureResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[PostureResponseService]**](PostureResponseService.md) |  | 

## Example

```python
from openziti_edge_client.models.posture_response import PostureResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponse from a JSON string
posture_response_instance = PostureResponse.from_json(json)
# print the JSON string representation of the object
print(PostureResponse.to_json())

# convert the object into a dict
posture_response_dict = posture_response_instance.to_dict()
# create an instance of PostureResponse from a dict
posture_response_from_dict = PostureResponse.from_dict(posture_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


