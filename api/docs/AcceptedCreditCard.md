# AcceptedCreditCard

Credit card code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**processing_country** | **str** | Country Code ISO | [optional] 

## Example

```python
from openapi_client.models.accepted_credit_card import AcceptedCreditCard

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedCreditCard from a JSON string
accepted_credit_card_instance = AcceptedCreditCard.from_json(json)
# print the JSON string representation of the object
print AcceptedCreditCard.to_json()

# convert the object into a dict
accepted_credit_card_dict = accepted_credit_card_instance.to_dict()
# create an instance of AcceptedCreditCard from a dict
accepted_credit_card_form_dict = accepted_credit_card.from_dict(accepted_credit_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


