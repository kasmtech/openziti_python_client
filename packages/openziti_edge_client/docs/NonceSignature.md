# NonceSignature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** |  | 
**ca_pool** | **str** |  | 
**kid** | **str** |  | 
**signature** | **str** |  | 

## Example

```python
from openziti_edge_client.models.nonce_signature import NonceSignature

# TODO update the JSON string below
json = "{}"
# create an instance of NonceSignature from a JSON string
nonce_signature_instance = NonceSignature.from_json(json)
# print the JSON string representation of the object
print(NonceSignature.to_json())

# convert the object into a dict
nonce_signature_dict = nonce_signature_instance.to_dict()
# create an instance of NonceSignature from a dict
nonce_signature_from_dict = NonceSignature.from_dict(nonce_signature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


