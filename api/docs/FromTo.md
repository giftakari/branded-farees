# FromTo

Location code

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**city_or_airport** | [**CityOrAirportEnum**](CityOrAirportEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.from_to import FromTo

# TODO update the JSON string below
json = "{}"
# create an instance of FromTo from a JSON string
from_to_instance = FromTo.from_json(json)
# print the JSON string representation of the object
print FromTo.to_json()

# convert the object into a dict
from_to_dict = from_to_instance.to_dict()
# create an instance of FromTo from a dict
from_to_form_dict = from_to.from_dict(from_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


