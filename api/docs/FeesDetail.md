# FeesDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | [**List[Fee]**](Fee.md) |  | [optional] 

## Example

```python
from openapi_client.models.fees_detail import FeesDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FeesDetail from a JSON string
fees_detail_instance = FeesDetail.from_json(json)
# print the JSON string representation of the object
print FeesDetail.to_json()

# convert the object into a dict
fees_detail_dict = fees_detail_instance.to_dict()
# create an instance of FeesDetail from a dict
fees_detail_form_dict = fees_detail.from_dict(fees_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


