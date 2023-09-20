# AgencyInfo

Detail of the travel agency that issues the ticket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticketed_date** | **str** | Ticketed date | [optional] 
**name** | **str** | Name of the Agency | 
**place** | **str** | Place of the agency | 
**ticketing_pcc** | **str** | Ticketing PCC | [optional] 
**code** | **str** | Agency code | [optional] 
**sales_type** | **str** | Sales type | [optional] 
**ticketing_country** | **str** | Ticketing country | 
**ticketing_city** | **str** | Ticketing city | 

## Example

```python
from openapi_client.models.agency_info import AgencyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyInfo from a JSON string
agency_info_instance = AgencyInfo.from_json(json)
# print the JSON string representation of the object
print AgencyInfo.to_json()

# convert the object into a dict
agency_info_dict = agency_info_instance.to_dict()
# create an instance of AgencyInfo from a dict
agency_info_form_dict = agency_info.from_dict(agency_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


