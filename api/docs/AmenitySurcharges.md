# AmenitySurcharges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**total_surcharges** | **float** | A monetary amount, up to 4 decimal places. Decimal place needs to be included. | [optional] 
**approximate_ind** | **bool** | if true, the surcharge amounts are approximate | [optional] 

## Example

```python
from openapi_client.models.amenity_surcharges import AmenitySurcharges

# TODO update the JSON string below
json = "{}"
# create an instance of AmenitySurcharges from a JSON string
amenity_surcharges_instance = AmenitySurcharges.from_json(json)
# print the JSON string representation of the object
print AmenitySurcharges.to_json()

# convert the object into a dict
amenity_surcharges_dict = amenity_surcharges_instance.to_dict()
# create an instance of AmenitySurcharges from a dict
amenity_surcharges_form_dict = amenity_surcharges.from_dict(amenity_surcharges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


