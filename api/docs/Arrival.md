# Arrival


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**location** | **str** | Location of departure or arrival | 
**var_date** | **date** | Local date of for arrival or departure | 
**time** | **str** | Local time Date of for arrival or departure | 

## Example

```python
from openapi_client.models.arrival import Arrival

# TODO update the JSON string below
json = "{}"
# create an instance of Arrival from a JSON string
arrival_instance = Arrival.from_json(json)
# print the JSON string representation of the object
print Arrival.to_json()

# convert the object into a dict
arrival_dict = arrival_instance.to_dict()
# create an instance of Arrival from a dict
arrival_form_dict = arrival.from_dict(arrival_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


