# EMDSegment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**sequence** | **int** | Sequence of EMDSegment | 
**quantity** | **int** | The quantity of the ancillary available on this EMDSegment | [optional] 
**emd_description** | [**EMDDescription**](EMDDescription.md) |  | [optional] 
**amount** | [**Amount**](Amount.md) |  | [optional] 
**status** | [**EMDStatusENUM**](EMDStatusENUM.md) |  | [optional] 
**date_of_service** | **str** | The date of service the service is available for | [optional] 
**present_to** | **str** | The airline the EMD should be presented to to supply the service | [optional] 
**present_at** | **str** | The location the EMD should be presented to to supply the service | [optional] 
**routing** | **str** | The routing the service is valid on | [optional] 

## Example

```python
from openapi_client.models.emd_segment import EMDSegment

# TODO update the JSON string below
json = "{}"
# create an instance of EMDSegment from a JSON string
emd_segment_instance = EMDSegment.from_json(json)
# print the JSON string representation of the object
print EMDSegment.to_json()

# convert the object into a dict
emd_segment_dict = emd_segment_instance.to_dict()
# create an instance of EMDSegment from a dict
emd_segment_form_dict = emd_segment.from_dict(emd_segment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


