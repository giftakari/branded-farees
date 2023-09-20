# Departure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**location** | **str** | Location of departure or arrival | 
**var_date** | **date** | Local date of for arrival or departure | 
**time** | **str** | Local time Date of for arrival or departure | 

## Example

```python
from openapi_client.models.departure import Departure

# TODO update the JSON string below
json = "{}"
# create an instance of Departure from a JSON string
departure_instance = Departure.from_json(json)
# print the JSON string representation of the object
print Departure.to_json()

# convert the object into a dict
departure_dict = departure_instance.to_dict()
# create an instance of Departure from a dict
departure_form_dict = departure.from_dict(departure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


