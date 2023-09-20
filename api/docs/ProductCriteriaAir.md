# ProductCriteriaAir


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**sequence** | **int** | Product criteria air sequence | 
**specific_flight_criteria** | [**List[SpecificFlightCriteria]**](SpecificFlightCriteria.md) |  | 

## Example

```python
from openapi_client.models.product_criteria_air import ProductCriteriaAir

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCriteriaAir from a JSON string
product_criteria_air_instance = ProductCriteriaAir.from_json(json)
# print the JSON string representation of the object
print ProductCriteriaAir.to_json()

# convert the object into a dict
product_criteria_air_dict = product_criteria_air_instance.to_dict()
# create an instance of ProductCriteriaAir from a dict
product_criteria_air_form_dict = product_criteria_air.from_dict(product_criteria_air_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


