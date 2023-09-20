# AgencyServiceFeeID


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**id** | **str** | Unique id for this object within a message | [optional] 

## Example

```python
from openapi_client.models.agency_service_fee_id import AgencyServiceFeeID

# TODO update the JSON string below
json = "{}"
# create an instance of AgencyServiceFeeID from a JSON string
agency_service_fee_id_instance = AgencyServiceFeeID.from_json(json)
# print the JSON string representation of the object
print AgencyServiceFeeID.to_json()

# convert the object into a dict
agency_service_fee_id_dict = agency_service_fee_id_instance.to_dict()
# create an instance of AgencyServiceFeeID from a dict
agency_service_fee_id_form_dict = agency_service_fee_id.from_dict(agency_service_fee_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


