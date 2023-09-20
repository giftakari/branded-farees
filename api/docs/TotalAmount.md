# TotalAmount


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
from openapi_client.models.total_amount import TotalAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TotalAmount from a JSON string
total_amount_instance = TotalAmount.from_json(json)
# print the JSON string representation of the object
print TotalAmount.to_json()

# convert the object into a dict
total_amount_dict = total_amount_instance.to_dict()
# create an instance of TotalAmount from a dict
total_amount_form_dict = total_amount.from_dict(total_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


