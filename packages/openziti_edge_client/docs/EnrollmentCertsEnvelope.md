# EnrollmentCertsEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EnrollmentCerts**](EnrollmentCerts.md) |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from openziti_edge_client.models.enrollment_certs_envelope import EnrollmentCertsEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollmentCertsEnvelope from a JSON string
enrollment_certs_envelope_instance = EnrollmentCertsEnvelope.from_json(json)
# print the JSON string representation of the object
print(EnrollmentCertsEnvelope.to_json())

# convert the object into a dict
enrollment_certs_envelope_dict = enrollment_certs_envelope_instance.to_dict()
# create an instance of EnrollmentCertsEnvelope from a dict
enrollment_certs_envelope_from_dict = EnrollmentCertsEnvelope.from_dict(enrollment_certs_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


