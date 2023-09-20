# Notification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_number** | [**List[QueueNumber]**](QueueNumber.md) |  | [optional] 
**var_date** | **date** | The notification date is equivalent to ticket time limit and will place the Reservation on the defined queue for the date specified. Sending a new notificiation date at commit step will update the existing notificationDate. Sending 000/00/00 will delete an existing notificationDate. | [optional] 

## Example

```python
from openapi_client.models.notification import Notification

# TODO update the JSON string below
json = "{}"
# create an instance of Notification from a JSON string
notification_instance = Notification.from_json(json)
# print the JSON string representation of the object
print Notification.to_json()

# convert the object into a dict
notification_dict = notification_instance.to_dict()
# create an instance of Notification from a dict
notification_form_dict = notification.from_dict(notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


