# RateDistance

Rate for the period defined by the attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**unlimited_distance_ind** | **bool** | Assigned Type: c-1100:OptionalIndicator | [optional] 
**requested_code_applied_ind** | **bool** | Assigned Type: c-1100:OptionalIndicator | [optional] 
**allowance** | **int** | Assigned Type: c-1100:NumberTripleDigit | [optional] 
**distance_units** | [**UnitOfDistanceEnum**](UnitOfDistanceEnum.md) |  | [optional] 
**rate_period** | [**RatePeriodEnum**](RatePeriodEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.rate_distance import RateDistance

# TODO update the JSON string below
json = "{}"
# create an instance of RateDistance from a JSON string
rate_distance_instance = RateDistance.from_json(json)
# print the JSON string representation of the object
print RateDistance.to_json()

# convert the object into a dict
rate_distance_dict = rate_distance_instance.to_dict()
# create an instance of RateDistance from a dict
rate_distance_form_dict = rate_distance.from_dict(rate_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


