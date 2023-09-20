# TermsAndConditionsID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Local indentifier within a given message for this object. | [optional] 
**terms_and_conditions_ref** | **str** | Used to reference another instance of this object in the same message. | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions_id import TermsAndConditionsID

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditionsID from a JSON string
terms_and_conditions_id_instance = TermsAndConditionsID.from_json(json)
# print the JSON string representation of the object
print TermsAndConditionsID.to_json()

# convert the object into a dict
terms_and_conditions_id_dict = terms_and_conditions_id_instance.to_dict()
# create an instance of TermsAndConditionsID from a dict
terms_and_conditions_id_form_dict = terms_and_conditions_id.from_dict(terms_and_conditions_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


