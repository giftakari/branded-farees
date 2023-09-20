# TermsAndConditionsFull


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_date** | **datetime** | The data and time the offer will expire | [optional] 
**customer_loyalty** | [**List[CustomerLoyalty]**](CustomerLoyalty.md) |  | [optional] 
**text_block** | [**List[TextBlock]**](TextBlock.md) |  | [optional] 

## Example

```python
from openapi_client.models.terms_and_conditions_full import TermsAndConditionsFull

# TODO update the JSON string below
json = "{}"
# create an instance of TermsAndConditionsFull from a JSON string
terms_and_conditions_full_instance = TermsAndConditionsFull.from_json(json)
# print the JSON string representation of the object
print TermsAndConditionsFull.to_json()

# convert the object into a dict
terms_and_conditions_full_dict = terms_and_conditions_full_instance.to_dict()
# create an instance of TermsAndConditionsFull from a dict
terms_and_conditions_full_form_dict = terms_and_conditions_full.from_dict(terms_and_conditions_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


