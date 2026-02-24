# AuthenticatorDetail

A singular authenticator resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**cert_pem** | **str** |  | [optional] 
**extend_requested_at** | **datetime** |  | [optional] 
**fingerprint** | **str** |  | [optional] 
**identity** | [**EntityRef**](EntityRef.md) |  | 
**identity_id** | **str** |  | 
**is_extend_requested** | **bool** |  | [optional] 
**is_issued_by_network** | **bool** |  | [optional] 
**is_key_roll_requested** | **bool** |  | [optional] 
**last_auth_resolved_to_root** | **bool** |  | [optional] 
**last_extend_rolled_keys** | **bool** |  | [optional] 
**method** | **str** |  | 
**username** | **str** |  | [optional] 

## Example

```python
from openziti_edge_client.models.authenticator_detail import AuthenticatorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDetail from a JSON string
authenticator_detail_instance = AuthenticatorDetail.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorDetail.to_json())

# convert the object into a dict
authenticator_detail_dict = authenticator_detail_instance.to_dict()
# create an instance of AuthenticatorDetail from a dict
authenticator_detail_from_dict = AuthenticatorDetail.from_dict(authenticator_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


