# DetailCurrentApiSessionCertificateEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CurrentApiSessionCertificateDetail**](CurrentApiSessionCertificateDetail.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openziti_edge_client.models.detail_current_api_session_certificate_envelope import DetailCurrentApiSessionCertificateEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DetailCurrentApiSessionCertificateEnvelope from a JSON string
detail_current_api_session_certificate_envelope_instance = DetailCurrentApiSessionCertificateEnvelope.from_json(json)
# print the JSON string representation of the object
print(DetailCurrentApiSessionCertificateEnvelope.to_json())

# convert the object into a dict
detail_current_api_session_certificate_envelope_dict = detail_current_api_session_certificate_envelope_instance.to_dict()
# create an instance of DetailCurrentApiSessionCertificateEnvelope from a dict
detail_current_api_session_certificate_envelope_from_dict = DetailCurrentApiSessionCertificateEnvelope.from_dict(detail_current_api_session_certificate_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


