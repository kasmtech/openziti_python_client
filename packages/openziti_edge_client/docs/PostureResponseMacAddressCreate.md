# PostureResponseMacAddressCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_addresses** | **List[str]** |  | 

## Example

```python
from openziti_edge_client.models.posture_response_mac_address_create import PostureResponseMacAddressCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PostureResponseMacAddressCreate from a JSON string
posture_response_mac_address_create_instance = PostureResponseMacAddressCreate.from_json(json)
# print the JSON string representation of the object
print(PostureResponseMacAddressCreate.to_json())

# convert the object into a dict
posture_response_mac_address_create_dict = posture_response_mac_address_create_instance.to_dict()
# create an instance of PostureResponseMacAddressCreate from a dict
posture_response_mac_address_create_from_dict = PostureResponseMacAddressCreate.from_dict(posture_response_mac_address_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


