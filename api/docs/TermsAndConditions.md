# TermsAndConditions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | The data and time the offer will expire | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions import TermsAndConditions

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditions from a JSON string
terms_and_conditions_instance = TermsAndConditions.from_json(json)
# print the JSON string representation of the object
print TermsAndConditions.to_json()

# convert the object into a dict
terms_and_conditions_dict = terms_and_conditions_instance.to_dict()
# create an instance of TermsAndConditions from a dict
terms_and_conditions_form_dict = terms_and_conditions.from_dict(terms_and_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


