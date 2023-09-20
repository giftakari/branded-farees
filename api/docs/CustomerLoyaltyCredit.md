# CustomerLoyaltyCredit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**customer_loyalty** | [**CustomerLoyalty**](CustomerLoyalty.md) |  | 
**earned** | **str** | Represents the amount of award credit awarded for this offer/offering. Award credit can be used for purchasing goods and services through a customer loyalty program | 
**status** | **str** | Represents the amount of status credit awarded for this offer/offering. Status credit allow a customer to move up the ladder of a customer loyalty program | 

## Example

```python
from openapi_client.models.customer_loyalty_credit import CustomerLoyaltyCredit

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerLoyaltyCredit from a JSON string
customer_loyalty_credit_instance = CustomerLoyaltyCredit.from_json(json)
# print the JSON string representation of the object
print CustomerLoyaltyCredit.to_json()

# convert the object into a dict
customer_loyalty_credit_dict = customer_loyalty_credit_instance.to_dict()
# create an instance of CustomerLoyaltyCredit from a dict
customer_loyalty_credit_form_dict = customer_loyalty_credit.from_dict(customer_loyalty_credit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


