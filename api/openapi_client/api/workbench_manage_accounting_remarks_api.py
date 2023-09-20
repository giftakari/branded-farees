# coding: utf-8

"""
    Akaris Travels Air

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 11.10.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictStr, constr

from typing import Optional

from openapi_client.models.accounting import Accounting
from openapi_client.models.accounting_response_wrapper import AccountingResponseWrapper

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class WorkbenchManageAccountingRemarksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_accounting(self, reservation_resource_identifier : Annotated[constr(strict=True, max_length=128), Field(..., description="Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.")], trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, accounting : Optional[Accounting] = None, **kwargs) -> AccountingResponseWrapper:  # noqa: E501
        """Add accounting remarks  # noqa: E501

        Accounting remarks are optional remarks that are added to the PNR and typically used by an agency's back office system in some way. The remarks can include ticket numbers, customer or account numbers, fares offered to the customer but refused, and canned remarks that document fare rules. Accounting remarks replace the back office accounting remarks in AirReservation prior to version 11.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_accounting(reservation_resource_identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, accounting, async_req=True)
        >>> result = thread.get()

        :param reservation_resource_identifier: Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. (required)
        :type reservation_resource_identifier: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param accounting:
        :type accounting: Accounting
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountingResponseWrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_accounting_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_accounting_with_http_info(reservation_resource_identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, accounting, **kwargs)  # noqa: E501

    @validate_arguments
    def create_accounting_with_http_info(self, reservation_resource_identifier : Annotated[constr(strict=True, max_length=128), Field(..., description="Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.")], trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, accounting : Optional[Accounting] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Add accounting remarks  # noqa: E501

        Accounting remarks are optional remarks that are added to the PNR and typically used by an agency's back office system in some way. The remarks can include ticket numbers, customer or account numbers, fares offered to the customer but refused, and canned remarks that document fare rules. Accounting remarks replace the back office accounting remarks in AirReservation prior to version 11.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_accounting_with_http_info(reservation_resource_identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, accounting, async_req=True)
        >>> result = thread.get()

        :param reservation_resource_identifier: Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. (required)
        :type reservation_resource_identifier: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param accounting:
        :type accounting: Accounting
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccountingResponseWrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'reservation_resource_identifier',
            'trace_id',
            'xauth_travelport_accessgroup',
            'travelport_plus_session_id',
            'accounting'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_accounting" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['reservation_resource_identifier']:
            _path_params['ReservationResource_Identifier'] = _params['reservation_resource_identifier']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['trace_id']:
            _header_params['TraceId'] = _params['trace_id']

        if _params['xauth_travelport_accessgroup']:
            _header_params['XAUTH_TRAVELPORT_ACCESSGROUP'] = _params['xauth_travelport_accessgroup']

        if _params['travelport_plus_session_id']:
            _header_params['TravelportPlusSessionID'] = _params['travelport_plus_session_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['accounting'] is not None:
            _body_params = _params['accounting']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '201': "AccountingResponseWrapper",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '402': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/book/accounting/reservationworkbench/{ReservationResource_Identifier}/accountings', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_accounting(self, reservation_resource_identifier : Annotated[constr(strict=True, max_length=128), Field(..., description="Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.")], id : Annotated[StrictStr, Field(..., description="The Accounting item id to be deleted")], name_value_pair_ids : Annotated[Optional[constr(strict=True, max_length=512)], Field(description="Comma separated list of nameValuePair IDs")] = None, trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> None:  # noqa: E501
        """Delete accounting remarks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_accounting(reservation_resource_identifier, id, name_value_pair_ids, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param reservation_resource_identifier: Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. (required)
        :type reservation_resource_identifier: str
        :param id: The Accounting item id to be deleted (required)
        :type id: str
        :param name_value_pair_ids: Comma separated list of nameValuePair IDs
        :type name_value_pair_ids: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_accounting_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_accounting_with_http_info(reservation_resource_identifier, id, name_value_pair_ids, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_accounting_with_http_info(self, reservation_resource_identifier : Annotated[constr(strict=True, max_length=128), Field(..., description="Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.")], id : Annotated[StrictStr, Field(..., description="The Accounting item id to be deleted")], name_value_pair_ids : Annotated[Optional[constr(strict=True, max_length=512)], Field(description="Comma separated list of nameValuePair IDs")] = None, trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete accounting remarks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_accounting_with_http_info(reservation_resource_identifier, id, name_value_pair_ids, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, async_req=True)
        >>> result = thread.get()

        :param reservation_resource_identifier: Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. (required)
        :type reservation_resource_identifier: str
        :param id: The Accounting item id to be deleted (required)
        :type id: str
        :param name_value_pair_ids: Comma separated list of nameValuePair IDs
        :type name_value_pair_ids: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'reservation_resource_identifier',
            'id',
            'name_value_pair_ids',
            'trace_id',
            'xauth_travelport_accessgroup',
            'travelport_plus_session_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_accounting" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['reservation_resource_identifier']:
            _path_params['ReservationResource_Identifier'] = _params['reservation_resource_identifier']

        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('name_value_pair_ids') is not None:  # noqa: E501
            _query_params.append(('NameValuePairIds', _params['name_value_pair_ids']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['trace_id']:
            _header_params['TraceId'] = _params['trace_id']

        if _params['xauth_travelport_accessgroup']:
            _header_params['XAUTH_TRAVELPORT_ACCESSGROUP'] = _params['xauth_travelport_accessgroup']

        if _params['travelport_plus_session_id']:
            _header_params['TravelportPlusSessionID'] = _params['travelport_plus_session_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/book/reservationworkbench/{ReservationResource_Identifier}/accountings/{id}/namevaluepairs', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_accounting(self, reservation_resource_identifier : Annotated[constr(strict=True, max_length=128), Field(..., description="Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.")], trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, accounting : Optional[Accounting] = None, **kwargs) -> AccountingResponseWrapper:  # noqa: E501
        """Update accounting remarks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_accounting(reservation_resource_identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, accounting, async_req=True)
        >>> result = thread.get()

        :param reservation_resource_identifier: Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. (required)
        :type reservation_resource_identifier: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param accounting:
        :type accounting: Accounting
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountingResponseWrapper
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_accounting_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_accounting_with_http_info(reservation_resource_identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, accounting, **kwargs)  # noqa: E501

    @validate_arguments
    def update_accounting_with_http_info(self, reservation_resource_identifier : Annotated[constr(strict=True, max_length=128), Field(..., description="Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database.")], trace_id : Annotated[Optional[StrictStr], Field(description="Identifier used to correlate API invocations across long-running or multi-call business flows.")] = None, xauth_travelport_accessgroup : Annotated[Optional[StrictStr], Field(description="Identifies the Travelport access group with which the caller is associated")] = None, travelport_plus_session_id : Annotated[Optional[StrictStr], Field(description="Travelport Plus Session ID used to maintain an established agency session")] = None, accounting : Optional[Accounting] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update accounting remarks  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_accounting_with_http_info(reservation_resource_identifier, trace_id, xauth_travelport_accessgroup, travelport_plus_session_id, accounting, async_req=True)
        >>> result = thread.get()

        :param reservation_resource_identifier: Identifier provides the ability to create a globally unique identifier. For the identifier to be globally unique it must have a system provided identifier and the system must be identified using a global naming authority. System identification uses the domain naming system (DNS) to assure they are globally unique and should be an URL. The system provided ID will typically be a primary or surrogate key in a database. (required)
        :type reservation_resource_identifier: str
        :param trace_id: Identifier used to correlate API invocations across long-running or multi-call business flows.
        :type trace_id: str
        :param xauth_travelport_accessgroup: Identifies the Travelport access group with which the caller is associated
        :type xauth_travelport_accessgroup: str
        :param travelport_plus_session_id: Travelport Plus Session ID used to maintain an established agency session
        :type travelport_plus_session_id: str
        :param accounting:
        :type accounting: Accounting
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccountingResponseWrapper, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'reservation_resource_identifier',
            'trace_id',
            'xauth_travelport_accessgroup',
            'travelport_plus_session_id',
            'accounting'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_accounting" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['reservation_resource_identifier']:
            _path_params['ReservationResource_Identifier'] = _params['reservation_resource_identifier']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['trace_id']:
            _header_params['TraceId'] = _params['trace_id']

        if _params['xauth_travelport_accessgroup']:
            _header_params['XAUTH_TRAVELPORT_ACCESSGROUP'] = _params['xauth_travelport_accessgroup']

        if _params['travelport_plus_session_id']:
            _header_params['TravelportPlusSessionID'] = _params['travelport_plus_session_id']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['accounting'] is not None:
            _body_params = _params['accounting']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "AccountingResponseWrapper",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '402': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '500': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/book/accounting/reservationworkbench/{ReservationResource_Identifier}/accountings', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
