# ClientExternalJwtSignerDetail

A External JWT Signer resource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, Link]**](Link.md) | A map of named links | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**tags** | [**Tags**](Tags.md) |  | [optional] 
**updated_at** | **datetime** |  | 
**audience** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**enroll_to_cert_enabled** | **bool** |  | [optional] 
**enroll_to_token_enabled** | **bool** |  | [optional] 
**external_auth_url** | **str** |  | 
**name** | **str** |  | 
**open_id_configuration_url** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**target_token** | [**TargetToken**](TargetToken.md) |  | [optional] 

## Example

```python
from openziti_edge_client.models.client_external_jwt_signer_detail import ClientExternalJwtSignerDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ClientExternalJwtSignerDetail from a JSON string
client_external_jwt_signer_detail_instance = ClientExternalJwtSignerDetail.from_json(json)
# print the JSON string representation of the object
print(ClientExternalJwtSignerDetail.to_json())

# convert the object into a dict
client_external_jwt_signer_detail_dict = client_external_jwt_signer_detail_instance.to_dict()
# create an instance of ClientExternalJwtSignerDetail from a dict
client_external_jwt_signer_detail_from_dict = ClientExternalJwtSignerDetail.from_dict(client_external_jwt_signer_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


