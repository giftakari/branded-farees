# AncillaryAirBaggage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baggage_type** | [**BaggageTypeEnum**](BaggageTypeEnum.md) |  | 
**measurement** | [**List[Measurement]**](Measurement.md) |  | 

## Example

```python
from openapi_client.models.ancillary_air_baggage import AncillaryAirBaggage

# TODO update the JSON string below
json = "{}"
# create an instance of AncillaryAirBaggage from a JSON string
ancillary_air_baggage_instance = AncillaryAirBaggage.from_json(json)
# print the JSON string representation of the object
print AncillaryAirBaggage.to_json()

# convert the object into a dict
ancillary_air_baggage_dict = ancillary_air_baggage_instance.to_dict()
# create an instance of AncillaryAirBaggage from a dict
ancillary_air_baggage_form_dict = ancillary_air_baggage.from_dict(ancillary_air_baggage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


