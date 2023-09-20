# ProductHospitality


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booking_code** | **str** | Booking code retrieved from the Availability response. | [optional] 
**guests** | **int** | Total number of guests | [optional] 
**more_rates_token** | **str** | More rates token | [optional] 
**ada_compliant** | [**YesNoUnknownEnum**](YesNoUnknownEnum.md) |  | [optional] 
**property_name** | **str** | The name of the hotel property | [optional] 
**property_key** | [**PropertyKey**](PropertyKey.md) |  | 
**room_type** | [**RoomType**](RoomType.md) |  | [optional] 
**date_range** | [**DateRange**](DateRange.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_hospitality import ProductHospitality

# TODO update the JSON string below
json = "{}"
# create an instance of ProductHospitality from a JSON string
product_hospitality_instance = ProductHospitality.from_json(json)
# print the JSON string representation of the object
print ProductHospitality.to_json()

# convert the object into a dict
product_hospitality_dict = product_hospitality_instance.to_dict()
# create an instance of ProductHospitality from a dict
product_hospitality_form_dict = product_hospitality.from_dict(product_hospitality_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


