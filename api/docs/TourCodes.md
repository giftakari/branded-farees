# TourCodes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**traveler_identifier_ref** | [**List[TravelerIdentifierRef]**](TravelerIdentifierRef.md) |  | [optional] 
**tour_code** | [**TourCode**](TourCode.md) |  | 

## Example

```python
from openapi_client.models.tour_codes import TourCodes

# TODO update the JSON string below
json = "{}"
# create an instance of TourCodes from a JSON string
tour_codes_instance = TourCodes.from_json(json)
# print the JSON string representation of the object
print TourCodes.to_json()

# convert the object into a dict
tour_codes_dict = tour_codes_instance.to_dict()
# create an instance of TourCodes from a dict
tour_codes_form_dict = tour_codes.from_dict(tour_codes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


