# TotpTokenEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TotpToken**](TotpToken.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.totp_token_envelope import TotpTokenEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TotpTokenEnvelope from a JSON string
totp_token_envelope_instance = TotpTokenEnvelope.from_json(json)
# print the JSON string representation of the object
print(TotpTokenEnvelope.to_json())

# convert the object into a dict
totp_token_envelope_dict = totp_token_envelope_instance.to_dict()
# create an instance of TotpTokenEnvelope from a dict
totp_token_envelope_from_dict = TotpTokenEnvelope.from_dict(totp_token_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


