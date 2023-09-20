# CO2EmissionsData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**actual** | [**Measurement**](Measurement.md) |  | [optional] 
**typical** | [**Measurement**](Measurement.md) |  | [optional] 
**variance** | **int** | The variance of CO2 emission from the typical emission value represented as a percentage. If positive the CO2 emission is higher than the industry average. If negative it is lower than the industry average | [optional] 

## Example

```python
from openapi_client.models.co2_emissions_data import CO2EmissionsData

# TODO update the JSON string below
json = "{}"
# create an instance of CO2EmissionsData from a JSON string
co2_emissions_data_instance = CO2EmissionsData.from_json(json)
# print the JSON string representation of the object
print CO2EmissionsData.to_json()

# convert the object into a dict
co2_emissions_data_dict = co2_emissions_data_instance.to_dict()
# create an instance of CO2EmissionsData from a dict
co2_emissions_data_form_dict = co2_emissions_data.from_dict(co2_emissions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


