# NightlyRate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**start_date** | **date** | Start date | 
**nights** | **int** | Number of nights this rate applies | [optional] 
**amount** | [**Amount**](Amount.md) |  | 

## Example

```python
from openapi_client.models.nightly_rate import NightlyRate

# TODO update the JSON string below
json = "{}"
# create an instance of NightlyRate from a JSON string
nightly_rate_instance = NightlyRate.from_json(json)
# print the JSON string representation of the object
print NightlyRate.to_json()

# convert the object into a dict
nightly_rate_dict = nightly_rate_instance.to_dict()
# create an instance of NightlyRate from a dict
nightly_rate_form_dict = nightly_rate.from_dict(nightly_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


