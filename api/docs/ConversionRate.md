# ConversionRate

A conversion metric from standard to another with the contextual authority such as IATA, OAG, ISO, etc.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**rate_authority** | **str** | Rate authority | [optional] 
**rate_as_of** | **datetime** | Rate as of | [optional] 

## Example

```python
from openapi_client.models.conversion_rate import ConversionRate

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionRate from a JSON string
conversion_rate_instance = ConversionRate.from_json(json)
# print the JSON string representation of the object
print ConversionRate.to_json()

# convert the object into a dict
conversion_rate_dict = conversion_rate_instance.to_dict()
# create an instance of ConversionRate from a dict
conversion_rate_form_dict = conversion_rate.from_dict(conversion_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


