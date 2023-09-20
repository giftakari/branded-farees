# openapi_client.WorkbenchManageReservationCommentsApi

All URIs are relative to *https://api.pp.travelport.com/11/air*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_reservation_comments**](WorkbenchManageReservationCommentsApi.md#add_reservation_comments) | **POST** /book/remarks/reservationworkbench/{ReservationResource_Identifier}/reservationcomments/list | Add Reservation Comments
[**delete_reservation_comments**](WorkbenchManageReservationCommentsApi.md#delete_reservation_comments) | **DELETE** /reservationworkbench/{ReservationResource_Identifier}/reservationcomments/{id}/comments | Delete Reservation Comments
[**update_reservation_comments**](WorkbenchManageReservationCommentsApi.md#update_reservation_comments) | **PUT** /book/remarks/reservationworkbench/{ReservationResource_Identifier}/reservationcomments | Update Reservation Comments


# **add_reservation_comments**
> ReservationCommentListResponseWrapper add_reservation_comments(reservation_resource_identifier, reservation_comment_list_request, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Add Reservation Comments

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_comment_list_request import ReservationCommentListRequest
from openapi_client.models.reservation_comment_list_response_wrapper import ReservationCommentListResponseWrapper
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
    api_instance = openapi_client.WorkbenchManageReservationCommentsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    reservation_comment_list_request = openapi_client.ReservationCommentListRequest() # ReservationCommentListRequest | 
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Add Reservation Comments
        api_response = api_instance.add_reservation_comments(reservation_resource_identifier, reservation_comment_list_request, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of WorkbenchManageReservationCommentsApi->add_reservation_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageReservationCommentsApi->add_reservation_comments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **reservation_comment_list_request** | [**ReservationCommentListRequest**](ReservationCommentListRequest.md)|  | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**ReservationCommentListResponseWrapper**](ReservationCommentListResponseWrapper.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created - 201 |  -  |
**400** | Bad Request- 400 |  -  |
**401** | Unauthorized - 401 |  -  |
**402** | PaymentRequired - 402 |  -  |
**403** | Forbidden - 403 |  -  |
**404** | Not Found - 404 |  -  |
**500** | Internal Server Error - 500 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reservation_comments**
> delete_reservation_comments(reservation_resource_identifier, id, comment_ids=comment_ids, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Delete Reservation Comments

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
    api_instance = openapi_client.WorkbenchManageReservationCommentsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    id = 'id_example' # str | The Reservation Comment ID to be deleted.
    comment_ids = 'comment_ids_example' # str | Comma separated list of comments IDs (optional)
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Delete Reservation Comments
        api_instance.delete_reservation_comments(reservation_resource_identifier, id, comment_ids=comment_ids, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
    except Exception as e:
        print("Exception when calling WorkbenchManageReservationCommentsApi->delete_reservation_comments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **id** | **str**| The Reservation Comment ID to be deleted. | 
 **comment_ids** | **str**| Comma separated list of comments IDs | [optional] 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

void (empty response body)

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

# **update_reservation_comments**
> ReservationCommentResponseWrapper update_reservation_comments(reservation_resource_identifier, reservation_comment, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)

Update Reservation Comments

### Example

* OAuth Authentication (OAuth2):
```python
import time
import os
import openapi_client
from openapi_client.models.reservation_comment import ReservationComment
from openapi_client.models.reservation_comment_response_wrapper import ReservationCommentResponseWrapper
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
    api_instance = openapi_client.WorkbenchManageReservationCommentsApi(api_client)
    reservation_resource_identifier = 'reservation_resource_identifier_example' # str | Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.
    reservation_comment = openapi_client.ReservationComment() # ReservationComment | Textual information.
    travelport_plus_session_id = 'travelport_plus_session_id_example' # str | Travelport Plus Session ID used to maintain an established agency session (optional)
    trace_id = 'trace_id_example' # str | Identifier used to correlate API invocations across long-running or multi-call business flows. (optional)
    xauth_travelport_accessgroup = 'xauth_travelport_accessgroup_example' # str | Identifies the Travelport access group with which the caller is associated (optional)

    try:
        # Update Reservation Comments
        api_response = api_instance.update_reservation_comments(reservation_resource_identifier, reservation_comment, travelport_plus_session_id=travelport_plus_session_id, trace_id=trace_id, xauth_travelport_accessgroup=xauth_travelport_accessgroup)
        print("The response of WorkbenchManageReservationCommentsApi->update_reservation_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkbenchManageReservationCommentsApi->update_reservation_comments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_resource_identifier** | **str**| Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. | 
 **reservation_comment** | [**ReservationComment**](ReservationComment.md)| Textual information. | 
 **travelport_plus_session_id** | **str**| Travelport Plus Session ID used to maintain an established agency session | [optional] 
 **trace_id** | **str**| Identifier used to correlate API invocations across long-running or multi-call business flows. | [optional] 
 **xauth_travelport_accessgroup** | **str**| Identifies the Travelport access group with which the caller is associated | [optional] 

### Return type

[**ReservationCommentResponseWrapper**](ReservationCommentResponseWrapper.md)

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

