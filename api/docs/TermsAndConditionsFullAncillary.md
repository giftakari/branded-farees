# TermsAndConditionsFullAncillary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_limit** | [**ApplicationLimit**](ApplicationLimit.md) |  | 
**refundability** | [**RefundabilityEnum**](RefundabilityEnum.md) |  | [optional] 
**unsellable_ind** | **bool** | If true, this ancillary product can not be sold through Travelport systems | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions_full_ancillary import TermsAndConditionsFullAncillary

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditionsFullAncillary from a JSON string
terms_and_conditions_full_ancillary_instance = TermsAndConditionsFullAncillary.from_json(json)
# print the JSON string representation of the object
print TermsAndConditionsFullAncillary.to_json()

# convert the object into a dict
terms_and_conditions_full_ancillary_dict = terms_and_conditions_full_ancillary_instance.to_dict()
# create an instance of TermsAndConditionsFullAncillary from a dict
terms_and_conditions_full_ancillary_form_dict = terms_and_conditions_full_ancillary.from_dict(terms_and_conditions_full_ancillary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


