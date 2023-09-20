# Amount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**currency_source** | [**CurrencySourceEnum**](CurrencySourceEnum.md) |  | [optional] 
**currency_code** | [**CurrencyCode**](CurrencyCode.md) |  | [optional] 
**base** | **float** | The price prior to all applicable taxes of a product such as the rate for a room or fare for a flight. | [optional] 
**taxes** | [**Taxes**](Taxes.md) |  | [optional] 
**fees** | [**Fees**](Fees.md) |  | [optional] 
**total** | **float** | Specifies the total price including base + taxes + fees | [optional] 
**approximate_ind** | **bool** | True if this amount has been converted from the original amount | [optional] 

## Example

```python
from openapi_client.models.amount import Amount

# TODO update the JSON string below
json = "{}"
# create an instance of Amount from a JSON string
amount_instance = Amount.from_json(json)
# print the JSON string representation of the object
print Amount.to_json()

# convert the object into a dict
amount_dict = amount_instance.to_dict()
# create an instance of Amount from a dict
amount_form_dict = amount.from_dict(amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


