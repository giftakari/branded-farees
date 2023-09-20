# TravelAgency


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_type** | [**OrganizationTypeEnum**](OrganizationTypeEnum.md) |  | [optional] 
**organization_name** | [**CompanyName**](CompanyName.md) |  | 
**corporate_code** | **str** | A reference assigned by the Travel Agency to identify the corporate organization | [optional] 
**profile_name** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.travel_agency import TravelAgency

# TODO update the JSON string below
json = "{}"
# create an instance of TravelAgency from a JSON string
travel_agency_instance = TravelAgency.from_json(json)
# print the JSON string representation of the object
print TravelAgency.to_json()

# convert the object into a dict
travel_agency_dict = travel_agency_instance.to_dict()
# create an instance of TravelAgency from a dict
travel_agency_form_dict = travel_agency.from_dict(travel_agency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


