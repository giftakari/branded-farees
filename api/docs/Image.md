# Image

URL of the image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**dimension_category** | **str** | Deprecated and replaced by Image Size | [optional] 
**width** | **int** | Width of image | [optional] 
**height** | **int** | Height | [optional] 
**caption** | **str** | Image title | [optional] 
**picture_category** | **int** | deprecated and replaced by pictureOf | [optional] 
**image_size** | [**ImageSizeEnum**](ImageSizeEnum.md) |  | [optional] 
**picture_of** | [**PictureofEnum**](PictureofEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.image import Image

# TODO update the JSON string below
json = "{}"
# create an instance of Image from a JSON string
image_instance = Image.from_json(json)
# print the JSON string representation of the object
print Image.to_json()

# convert the object into a dict
image_dict = image_instance.to_dict()
# create an instance of Image from a dict
image_form_dict = image.from_dict(image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


