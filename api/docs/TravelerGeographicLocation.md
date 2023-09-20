# TravelerGeographicLocation

Specifies which location the Traveler resides in. Used for resident fares

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**traveler_geographic_location_type** | [**TravelerGeographicTypeEnum**](TravelerGeographicTypeEnum.md) |  | [optional] 
**resident_geographic_code** | **str** | Resident code, currently used to handle Spanish residency fares for NDC channel where this code is required in addition to the city of residence | [optional] 
**general_large_family_resident_discount_ind** | **bool** | if true, this request qualifies for general large family resident discount. General large families (up to 3 children) from Spain, from the EU/EEA or of any other nationality, whose residency in Spain is recognised and who are in possession of a large-family certificate issued by the autonomous community in which they live. | [optional] 
**special_large_family_resident_discount_ind** | **bool** | if true, this request qualifies for special large family resident discount. Special large families (4 or more children) from Spain, from the EU/EEA or of any other nationality, whose residency in Spain is recognised and who are in possession of a large-family certificate issued by the autonomous community in which they live. | [optional] 

## Example

```python
from openapi_client.models.traveler_geographic_location import TravelerGeographicLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TravelerGeographicLocation from a JSON string
traveler_geographic_location_instance = TravelerGeographicLocation.from_json(json)
# print the JSON string representation of the object
print TravelerGeographicLocation.to_json()

# convert the object into a dict
traveler_geographic_location_dict = traveler_geographic_location_instance.to_dict()
# create an instance of TravelerGeographicLocation from a dict
traveler_geographic_location_form_dict = traveler_geographic_location.from_dict(traveler_geographic_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


