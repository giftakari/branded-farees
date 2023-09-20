# SupplierRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**base_rate** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**rate_for_period** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**drop_off_charge** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**extra_mileage_charge** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 
**estimated_total_amount** | [**CurrencyAmount**](CurrencyAmount.md) |  | [optional] 

## Example

```python
from openapi_client.models.supplier_rate import SupplierRate

# TODO update the JSON string below
json = "{}"
# create an instance of SupplierRate from a JSON string
supplier_rate_instance = SupplierRate.from_json(json)
# print the JSON string representation of the object
print SupplierRate.to_json()

# convert the object into a dict
supplier_rate_dict = supplier_rate_instance.to_dict()
# create an instance of SupplierRate from a dict
supplier_rate_form_dict = supplier_rate.from_dict(supplier_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


