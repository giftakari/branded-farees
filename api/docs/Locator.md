# Locator

Contains the locator (PNR or external locator) or cancellation number for the reservation, order, or offer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**locator_type** | **str** | Specifies the type of reservation ID | [optional] 
**source** | **str** | Specifies a unique identifier to indicate the source system which generated the resid | [optional] 
**source_context** | **str** | Specifies the context of the source | [optional] 
**ota_type** | **str** | Used for codes | [optional] 
**creation_date** | **date** | Reservation Creation date | [optional] 

## Example

```python
from openapi_client.models.locator import Locator

# TODO update the JSON string below
json = "{}"
# create an instance of Locator from a JSON string
locator_instance = Locator.from_json(json)
# print the JSON string representation of the object
print Locator.to_json()

# convert the object into a dict
locator_dict = locator_instance.to_dict()
# create an instance of Locator from a dict
locator_form_dict = locator.from_dict(locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


