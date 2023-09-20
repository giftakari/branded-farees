# openapi_client.WorkbenchManagementApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reservation_workbench**](WorkbenchManagementApi.md#create_reservation_workbench) | **POST** /book/session/reservationworkbench | Create a workbench for new booking
[**create_reservation_workbench_from_identifier**](WorkbenchManagementApi.md#create_reservation_workbench_from_identifier) | **POST** /book/session/reservationworkbench/buildfromidentifier/{Identifier} | Create a workbench for existing booking
[**create_reservation_workbench_from_locator**](WorkbenchManagementApi.md#create_reservation_workbench_from_locator) | **POST** /book/session/reservationworkbench/buildfromlocator | Create a workbench for existing booking
[**ignore_reservation_workbench**](WorkbenchManagementApi.md#ignore_reservation_workbench) | **DELETE** /book/session/reservationworkbench/{Identifier} | Discard workbench
[**retrieve_reservation_workbench**](WorkbenchManagementApi.md#retrieve_reservation_workbench) | **GET** /book/session/reservationworkbench/{Identifier} | Retrieve workbench details


# **create_reservation_workbench**
> ReservationResponseWrapper create_reservation_workbench(reservation_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Create a workbench for new booking

Use this request to initiate a workbench for a new reservation. This prerequisite step for booking creates the workbench session in which all booking details are added together to create a PNR at commit.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_id import ReservationID
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.WorkbenchManagementApi(api_client)
    reservation_id = openapi_client.ReservationID() # ReservationID | 
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Create a workbench for new booking
        api_response = api_instance.create_reservation_workbench(reservation_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of WorkbenchManagementApi->create_reservation_workbench:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManagementApi->create_reservation_workbench: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | [**ReservationID**](ReservationID.md)|  | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reservation_workbench_from_identifier**
> ReservationResponseWrapper create_reservation_workbench_from_identifier(identifier, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, identifier_type=identifier_type, document_type=document_type, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Create a workbench for existing booking

Initiate a post-commit workbench to create a session for ticketing or updating an existing reservation. This is a prerequisite step for any transaction that modifies, updates, or tickets any PNR.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.document_type_enum import DocumentTypeEnum
from openapi_client.models.identifier_type_enum import IdentifierTypeENUM
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.WorkbenchManagementApi(api_client)
    identifier = 'identifier_example' # str | 
    detail_view_ind = True # bool |  (optional)
    view_brand_complete_info_ind = True # bool | If true, Brand complete information will be returned in Reservation Response (optional)
    view_baggage_detail_ind = True # bool | if true, full baggage information will be returned in Reservation Response (optional)
    identifier_type = openapi_client.IdentifierTypeENUM() # IdentifierTypeENUM | The type of identifier key used to retrieve the reservation (optional)
    document_type = openapi_client.DocumentTypeEnum() # DocumentTypeEnum | When document is selected in IdentifierType, use documentType to identify the type of document (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Create a workbench for existing booking
        api_response = api_instance.create_reservation_workbench_from_identifier(identifier, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, identifier_type=identifier_type, document_type=document_type, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of WorkbenchManagementApi->create_reservation_workbench_from_identifier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManagementApi->create_reservation_workbench_from_identifier: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **detail_view_ind** | **bool**|  | [optional] 
 **view_brand_complete_info_ind** | **bool**| If true, Brand complete information will be returned in Reservation Response | [optional] 
 **view_baggage_detail_ind** | **bool**| if true, full baggage information will be returned in Reservation Response | [optional] 
 **identifier_type** | [**IdentifierTypeENUM**](.md)| The type of identifier key used to retrieve the reservation | [optional] 
 **document_type** | [**DocumentTypeEnum**](.md)| When document is selected in IdentifierType, use documentType to identify the type of document | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reservation_workbench_from_locator**
> ReservationResponseWrapper create_reservation_workbench_from_locator(locator=locator, source=source, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Create a workbench for existing booking

Initiate a post-commit workbench to create a session for ticketing or updating an existing reservation. This is a prerequisite step for any transaction that modifies, updates, or tickets any PNR.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.WorkbenchManagementApi(api_client)
    locator = 'locator_example' # str |  (optional)
    source = 'source_example' # str | Specifies a unique identifier to indicate the source system which generated the resId. (optional)
    detail_view_ind = True # bool | If true, ReservationDetail will be returned (optional)
    view_brand_complete_info_ind = True # bool | If true, Brand complete information will be returned in Reservation Response (optional)
    view_baggage_detail_ind = True # bool | if true, full baggage information will be returned in Reservation Response (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Create a workbench for existing booking
        api_response = api_instance.create_reservation_workbench_from_locator(locator=locator, source=source, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of WorkbenchManagementApi->create_reservation_workbench_from_locator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManagementApi->create_reservation_workbench_from_locator: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locator** | **str**|  | [optional] 
 **source** | **str**| Specifies a unique identifier to indicate the source system which generated the resId. | [optional] 
 **detail_view_ind** | **bool**| If true, ReservationDetail will be returned | [optional] 
 **view_brand_complete_info_ind** | **bool**| If true, Brand complete information will be returned in Reservation Response | [optional] 
 **view_baggage_detail_ind** | **bool**| if true, full baggage information will be returned in Reservation Response | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK - Successful Response - 200 |  -  |
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ignore_reservation_workbench**
> ignore_reservation_workbench(identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Discard workbench

At any point in a booking or ticketing workflow, if necessary, you can discard the workbench and any information in it.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.WorkbenchManagementApi(api_client)
    identifier = 'identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Discard workbench
        api_instance.ignore_reservation_workbench(identifier, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
    except Exception as e:
        print("Exception when calling WorkbenchManagementApi->ignore_reservation_workbench: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  OK - Successful Response - 200 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_reservation_workbench**
> ReservationResponseWrapper retrieve_reservation_workbench(identifier, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)

Retrieve workbench details

At any point in the booking session, you can retrieve the workbench. The response returns all details added to the workbench at that point.

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_response_wrapper import ReservationResponseWrapper
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
    api_instance = openapi_client.WorkbenchManagementApi(api_client)
    identifier = 'identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    detail_view_ind = True # bool | If true, ReservationDetail will be returned. (optional)
    view_brand_complete_info_ind = True # bool | If true, Brand complete information will be returned in Reservation Response (optional)
    view_baggage_detail_ind = True # bool | if true, full baggage information will be returned in Reservation Response (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)

    try:
        # Retrieve workbench details
        api_response = api_instance.retrieve_reservation_workbench(identifier, detail_view_ind=detail_view_ind, view_brand_complete_info_ind=view_brand_complete_info_ind, view_baggage_detail_ind=view_baggage_detail_ind, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup, travelport_plus_session_id=travelport_plus_session_id)
        print("The response of WorkbenchManagementApi->retrieve_reservation_workbench:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManagementApi->retrieve_reservation_workbench: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **detail_view_ind** | **bool**| If true, ReservationDetail will be returned. | [optional] 
 **view_brand_complete_info_ind** | **bool**| If true, Brand complete information will be returned in Reservation Response | [optional] 
 **view_baggage_detail_ind** | **bool**| if true, full baggage information will be returned in Reservation Response | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 

### Return type

[**ReservationResponseWrapper**](ReservationResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  OK - Successful Response - 200 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

