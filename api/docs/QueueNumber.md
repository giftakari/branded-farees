# QueueNumber

The queue number

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**category** | **str** | The Queue Category | [optional] 
**sub_category** | **str** | Date range subCategory | [optional] 
**override_pcc** | **str** | Use PCC to override to queue the Reservation to another PCC | [optional] 

## Example

```python
from openapi_client.models.queue_number import QueueNumber

# TODO update the JSON string below
json = "{}"
# create an instance of QueueNumber from a JSON string
queue_number_instance = QueueNumber.from_json(json)
# print the JSON string representation of the object
print QueueNumber.to_json()

# convert the object into a dict
queue_number_dict = queue_number_instance.to_dict()
# create an instance of QueueNumber from a dict
queue_number_form_dict = queue_number.from_dict(queue_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


