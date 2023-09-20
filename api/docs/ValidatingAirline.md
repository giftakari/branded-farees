# ValidatingAirline


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**segment_sequence_list** | **List[int]** | The segmentSequenceList the validatingCarrier applies to | [optional] 
**validating_airline** | **str** | Represents the airline responsible for ticketing/fulfillment of this Offer | 
**product_ref** | **List[str]** | The productRef the validatingCarrier applies to | [optional] 

## Example

```python
from openapi_client.models.validating_airline import ValidatingAirline

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatingAirline from a JSON string
validating_airline_instance = ValidatingAirline.from_json(json)
# print the JSON string representation of the object
print ValidatingAirline.to_json()

# convert the object into a dict
validating_airline_dict = validating_airline_instance.to_dict()
# create an instance of ValidatingAirline from a dict
validating_airline_form_dict = validating_airline.from_dict(validating_airline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


