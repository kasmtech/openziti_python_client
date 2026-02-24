# DetailMfaRecoveryCodesEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DetailMfaRecoveryCodes**](DetailMfaRecoveryCodes.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_management.models.detail_mfa_recovery_codes_envelope import DetailMfaRecoveryCodesEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailMfaRecoveryCodesEnvelope from a JSON string
detail_mfa_recovery_codes_envelope_instance = DetailMfaRecoveryCodesEnvelope.from_json(json)
# print the JSON string representation of the object
print(DetailMfaRecoveryCodesEnvelope.to_json())

# convert the object into a dict
detail_mfa_recovery_codes_envelope_dict = detail_mfa_recovery_codes_envelope_instance.to_dict()
# create an instance of DetailMfaRecoveryCodesEnvelope from a dict
detail_mfa_recovery_codes_envelope_from_dict = DetailMfaRecoveryCodesEnvelope.from_dict(detail_mfa_recovery_codes_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


