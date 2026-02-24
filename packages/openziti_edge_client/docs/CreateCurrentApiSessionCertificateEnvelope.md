# CreateCurrentApiSessionCertificateEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrentApiSessionCertificateCreateResponse**](CurrentApiSessionCertificateCreateResponse.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.create_current_api_session_certificate_envelope import CreateCurrentApiSessionCertificateEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCurrentApiSessionCertificateEnvelope from a JSON string
create_current_api_session_certificate_envelope_instance = CreateCurrentApiSessionCertificateEnvelope.from_json(json)
# print the JSON string representation of the object
print(CreateCurrentApiSessionCertificateEnvelope.to_json())

# convert the object into a dict
create_current_api_session_certificate_envelope_dict = create_current_api_session_certificate_envelope_instance.to_dict()
# create an instance of CreateCurrentApiSessionCertificateEnvelope from a dict
create_current_api_session_certificate_envelope_from_dict = CreateCurrentApiSessionCertificateEnvelope.from_dict(create_current_api_session_certificate_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


