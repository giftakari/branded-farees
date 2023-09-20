# Surcharge

The fee amount with feecode and reporting informtion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**currency_code** | **str** | Sur charge currency code | [optional] 
**surcharge_code** | **str** | Sur charge code | [optional] 
**reporting_authority** | **str** | Sur charge reporting authority | [optional] 
**purpose** | **str** | Sur charge purpose | [optional] 
**description** | **str** | Description | [optional] 
**surcharge_application** | [**ApplicationEnum**](ApplicationEnum.md) |  | [optional] 
**surcharge_frequency** | [**FrequencyEnum**](FrequencyEnum.md) |  | [optional] 
**code_authority** | **str** | Surcharge code authority | [optional] 
**decimal_place** | **int** | Decimal place for the currency unit | [optional] 
**decimal_authority** | **str** | Currency code decimal authority | [optional] 

## Example

```python
from openapi_client.models.surcharge import Surcharge

# TODO update the JSON string below
json = "{}"
# create an instance of Surcharge from a JSON string
surcharge_instance = Surcharge.from_json(json)
# print the JSON string representation of the object
print Surcharge.to_json()

# convert the object into a dict
surcharge_dict = surcharge_instance.to_dict()
# create an instance of Surcharge from a dict
surcharge_form_dict = surcharge.from_dict(surcharge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


