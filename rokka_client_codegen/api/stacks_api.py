# coding: utf-8

"""
    rokka.io

    digital image processing done right. [Documentation](https://rokka.io/documentation). [Changelog](https://api.rokka.io/changelog.md).  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rokka_client_codegen.api_client import ApiClient


class StacksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_stack(self, stack_definition, organization, name, **kwargs):  # noqa: E501
        """Create a new stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_stack(stack_definition, organization, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StackDefinition stack_definition: Stack operations and options definition. See https://rokka.io/documentation/references/stacks.html for explanations how to define stacks. (required)
        :param str organization: (required)
        :param str name: (required)
        :param bool overwrite: Whether to overwrite the stack if it already exists
        :return: Stack
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_stack_with_http_info(stack_definition, organization, name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_stack_with_http_info(stack_definition, organization, name, **kwargs)  # noqa: E501
            return data

    def create_stack_with_http_info(self, stack_definition, organization, name, **kwargs):  # noqa: E501
        """Create a new stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_stack_with_http_info(stack_definition, organization, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param StackDefinition stack_definition: Stack operations and options definition. See https://rokka.io/documentation/references/stacks.html for explanations how to define stacks. (required)
        :param str organization: (required)
        :param str name: (required)
        :param bool overwrite: Whether to overwrite the stack if it already exists
        :return: Stack
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stack_definition', 'organization', 'name', 'overwrite']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_stack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stack_definition' is set
        if ('stack_definition' not in params or
                params['stack_definition'] is None):
            raise ValueError("Missing the required parameter `stack_definition` when calling `create_stack`")  # noqa: E501
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `create_stack`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `create_stack`")  # noqa: E501

        if 'organization' in params and not re.search(r'[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `create_stack`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        if 'name' in params and not re.search(r'[A-Za-z0-9\\-_]+', params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `create_stack`, must conform to the pattern `/[A-Za-z0-9\\-_]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []
        if 'overwrite' in params:
            query_params.append(('overwrite', params['overwrite']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'stack_definition' in params:
            body_params = params['stack_definition']
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stacks/{organization}/{name}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Stack',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_stack(self, organization, name, **kwargs):  # noqa: E501
        """Delete a stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_stack(organization, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization: (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_stack_with_http_info(organization, name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_stack_with_http_info(organization, name, **kwargs)  # noqa: E501
            return data

    def delete_stack_with_http_info(self, organization, name, **kwargs):  # noqa: E501
        """Delete a stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_stack_with_http_info(organization, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization: (required)
        :param str name: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_stack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `delete_stack`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `delete_stack`")  # noqa: E501

        if 'organization' in params and not re.search(r'[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `delete_stack`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        if 'name' in params and not re.search(r'[A-Za-z0-9\\-_]+', params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `delete_stack`, must conform to the pattern `/[A-Za-z0-9\\-_]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stacks/{organization}/{name}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stack(self, organization, name, **kwargs):  # noqa: E501
        """Get a single stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stack(organization, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization: (required)
        :param str name: (required)
        :return: Stack
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stack_with_http_info(organization, name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stack_with_http_info(organization, name, **kwargs)  # noqa: E501
            return data

    def get_stack_with_http_info(self, organization, name, **kwargs):  # noqa: E501
        """Get a single stack.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stack_with_http_info(organization, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization: (required)
        :param str name: (required)
        :return: Stack
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `get_stack`")  # noqa: E501
        # verify the required parameter 'name' is set
        if ('name' not in params or
                params['name'] is None):
            raise ValueError("Missing the required parameter `name` when calling `get_stack`")  # noqa: E501

        if 'organization' in params and not re.search(r'[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `get_stack`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        if 'name' in params and not re.search(r'[A-Za-z0-9\\-_]+', params['name']):  # noqa: E501
            raise ValueError("Invalid value for parameter `name` when calling `get_stack`, must conform to the pattern `/[A-Za-z0-9\\-_]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stacks/{organization}/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Stack',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_operations(self, **kwargs):  # noqa: E501
        """Listing all available operations that can be used in stacks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_operations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, StackOperationDescription)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_operations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_operations_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_operations_with_http_info(self, **kwargs):  # noqa: E501
        """Listing all available operations that can be used in stacks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_operations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: dict(str, StackOperationDescription)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_operations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/operations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, StackOperationDescription)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_stack_options(self, **kwargs):  # noqa: E501
        """List all available options that can be set on stacks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_stack_options(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StackOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_stack_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_stack_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_stack_options_with_http_info(self, **kwargs):  # noqa: E501
        """List all available options that can be set on stacks.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_stack_options_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: StackOptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_stack_options" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stackoptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StackOptions',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_stacks(self, organization, **kwargs):  # noqa: E501
        """Get all stacks of an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_stacks(organization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization: (required)
        :param int limit: How many stacks should be returned
        :param str offset: When paging results, where to start. Must be a cursor, absolute numbers are not supported
        :return: ListStacksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_stacks_with_http_info(organization, **kwargs)  # noqa: E501
        else:
            (data) = self.list_stacks_with_http_info(organization, **kwargs)  # noqa: E501
            return data

    def list_stacks_with_http_info(self, organization, **kwargs):  # noqa: E501
        """Get all stacks of an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_stacks_with_http_info(organization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str organization: (required)
        :param int limit: How many stacks should be returned
        :param str offset: When paging results, where to start. Must be a cursor, absolute numbers are not supported
        :return: ListStacksResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_stacks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `list_stacks`")  # noqa: E501

        if 'organization' in params and not re.search(r'[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `list_stacks`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        if 'limit' in params and params['limit'] > 2000:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_stacks`, must be a value less than or equal to `2000`")  # noqa: E501
        if 'limit' in params and params['limit'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_stacks`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/stacks/{organization}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListStacksResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
