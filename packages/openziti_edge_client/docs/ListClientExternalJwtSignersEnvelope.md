# ListClientExternalJwtSignersEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientExternalJwtSignerDetail]**](ClientExternalJwtSignerDetail.md) | An array of External JWT Signers resources | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.list_client_external_jwt_signers_envelope import ListClientExternalJwtSignersEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListClientExternalJwtSignersEnvelope from a JSON string
list_client_external_jwt_signers_envelope_instance = ListClientExternalJwtSignersEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListClientExternalJwtSignersEnvelope.to_json())

# convert the object into a dict
list_client_external_jwt_signers_envelope_dict = list_client_external_jwt_signers_envelope_instance.to_dict()
# create an instance of ListClientExternalJwtSignersEnvelope from a dict
list_client_external_jwt_signers_envelope_from_dict = ListClientExternalJwtSignersEnvelope.from_dict(list_client_external_jwt_signers_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


