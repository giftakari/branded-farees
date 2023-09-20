# TravelAgencyID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Simple xsd id, not for external use | [optional] 
**travel_organization_ref** | **str** | An organization that has a name and a structure and members and directly works in the travel industry | [optional] 
**identifier** | [**Identifier**](Identifier.md) |  | [optional] 

## Example

```python
from openapi_client.models.travel_agency_id import TravelAgencyID

# TODO update the JSON string below
json = "{}"
# create an instance of TravelAgencyID from a JSON string
travel_agency_id_instance = TravelAgencyID.from_json(json)
# print the JSON string representation of the object
print TravelAgencyID.to_json()

# convert the object into a dict
travel_agency_id_dict = travel_agency_id_instance.to_dict()
# create an instance of TravelAgencyID from a dict
travel_agency_id_form_dict = travel_agency_id.from_dict(travel_agency_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


