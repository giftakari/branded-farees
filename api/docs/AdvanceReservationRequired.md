# AdvanceReservationRequired


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instant_purchase** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | 
**standby** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | 
**waiver_date** | **str** | Waiver date | [optional] 
**reservation_travel_segment_indicator_atpco** | **int** | The ATPCO travel segment geographic indicator. Example&#x3D; 1st segment over the water | [optional] 
**confirmed_status** | [**List[ConfirmedStatusEnum]**](ConfirmedStatusEnum.md) |  | [optional] 
**waitlist_standby_condition** | [**List[WaitlistStandbyConditionEnum]**](WaitlistStandbyConditionEnum.md) |  | [optional] 
**first_reservation** | [**FirstReservation**](FirstReservation.md) |  | 
**last_reservation** | [**LastReservation**](LastReservation.md) |  | 

## Example

```python
from openapi_client.models.advance_reservation_required import AdvanceReservationRequired

# TODO update the JSON string below
json = "{}"
# create an instance of AdvanceReservationRequired from a JSON string
advance_reservation_required_instance = AdvanceReservationRequired.from_json(json)
# print the JSON string representation of the object
print AdvanceReservationRequired.to_json()

# convert the object into a dict
advance_reservation_required_dict = advance_reservation_required_instance.to_dict()
# create an instance of AdvanceReservationRequired from a dict
advance_reservation_required_form_dict = advance_reservation_required.from_dict(advance_reservation_required_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


