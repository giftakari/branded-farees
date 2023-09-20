# Measurement

Used for dimensional units (width, height, depth) or weight

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**measurement_type** | [**MeasurementTypeEnum**](MeasurementTypeEnum.md) |  | [optional] 
**unit** | [**UnitOfMeasureEnum**](UnitOfMeasureEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.measurement import Measurement

# TODO update the JSON string below
json = "{}"
# create an instance of Measurement from a JSON string
measurement_instance = Measurement.from_json(json)
# print the JSON string representation of the object
print Measurement.to_json()

# convert the object into a dict
measurement_dict = measurement_instance.to_dict()
# create an instance of Measurement from a dict
measurement_form_dict = measurement.from_dict(measurement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


