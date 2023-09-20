# openapi_client.EMDApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**e_md_get_by_locator**](EMDApi.md#e_md_get_by_locator) | **GET** /emds/getbylocator | Retrieve EMD by locator
[**get_emd**](EMDApi.md#get_emd) | **GET** /emds/{Identifier} | Retrieve an EMD
[**update_emd**](EMDApi.md#update_emd) | **PUT** /emds/{Identifier} | Void an EMD


# **e_md_get_by_locator**
> EMDListResponseWrapper e_md_get_by_locator(locator, locator_type=locator_type, source=source, source_context=source_context, ota_type=ota_type, creation_date=creation_date, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Retrieve EMD by locator

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.emd_list_response_wrapper import EMDListResponseWrapper
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMDApi(api_client)
    locator = 'locator_example' # str | 
    locator_type = 'locator_type_example' # str | Specifies the type of reservation ID (e.g. reservation or cancellation). (optional)
    source = 'source_example' # str | Specifies a unique identifier to indicate the source system which generated the resId. (optional)
    source_context = 'source_context_example' # str | Specifies the context of the source. (optional)
    ota_type = 'ota_type_example' # str | Used for codes in the OpenTravel Code tables. Possible values of this pattern are 1, 101, 101.EQP, or 101.EQP.X. (optional)
    creation_date = '2013-10-20' # date | PNR creation Date (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Retrieve EMD by locator
        api_response = api_instance.e_md_get_by_locator(locator, locator_type=locator_type, source=source, source_context=source_context, ota_type=ota_type, creation_date=creation_date, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of EMDApi->e_md_get_by_locator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMDApi->e_md_get_by_locator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | 
 **locator_type** | **str**| Specifies the type of reservation ID (e.g. reservation or cancellation). | [optional] 
 **source** | **str**| Specifies a unique identifier to indicate the source system which generated the resId. | [optional] 
 **source_context** | **str**| Specifies the context of the source. | [optional] 
 **ota_type** | **str**| Used for codes in the OpenTravel Code tables. Possible values of this pattern are 1, 101, 101.EQP, or 101.EQP.X. | [optional] 
 **creation_date** | **date**| PNR creation Date | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**EMDListResponseWrapper**](EMDListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emd**
> EMDListResponseWrapper get_emd(identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Retrieve an EMD

Display an EMD to retrieve EMD details such as the amount paid and agency ticketing information.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.emd_list_response_wrapper import EMDListResponseWrapper
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMDApi(api_client)
    identifier = 'identifier_example' # str | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Retrieve an EMD
        api_response = api_instance.get_emd(identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of EMDApi->get_emd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMDApi->get_emd: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**EMDListResponseWrapper**](EMDListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_emd**
> EMDListResponseWrapper update_emd(identifier, emd_query_update_emd, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Void an EMD

Void an EMD to cancel it. You can also use EMD void with GDS Exchange Ticketing API to refund an EMD back to the FOP.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.emd_list_response_wrapper import EMDListResponseWrapper
from openapi_client.models.emd_query_update_emd import EMDQueryUpdateEMD
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pp.travelport.com/11/air
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pp.travelport.com/11/air"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMDApi(api_client)
    identifier = 'identifier_example' # str | 
    emd_query_update_emd = openapi_client.EMDQueryUpdateEMD() # EMDQueryUpdateEMD | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Void an EMD
        api_response = api_instance.update_emd(identifier, emd_query_update_emd, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of EMDApi->update_emd:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMDApi->update_emd: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **emd_query_update_emd** | [**EMDQueryUpdateEMD**](EMDQueryUpdateEMD.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**EMDListResponseWrapper**](EMDListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

