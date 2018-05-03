# rokka-client-codegen

This Python package for rokka.io was automatically generated by [Swagger Codegen](https://github.com/swagger-api/swagger-codegen).

See the [examples](examples/) directory for some simple rokka specific examples.

A thin wrapper package for using this to make some things easier would be welcome. We're [happy to help](https://rokka.io/en/contact/).

The pip is currently nowhere published, you have to build it yourself (see below). But if needed, we will publish it.

- API version: 1.0.0
- Package version: 0.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/rokka-io/rokka-python-codegen.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/rokka-io/rokka-python-codegen.git`)

Then import the package:
```python
import rokka_client_codegen 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import rokka_client_codegen
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then see the [examples](examples/)  directory.

## Documentation for API Endpoints

All URIs are relative to *https://api.rokka.io/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**create_membership**](docs/AdminApi.md#create_membership) | **PUT** /organizations/{organization}/memberships/{email} | Add a rokka user into an organization.
*AdminApi* | [**create_organization**](docs/AdminApi.md#create_organization) | **PUT** /organizations/{organization} | Register a new Organization.
*AdminApi* | [**create_organization_options**](docs/AdminApi.md#create_organization_options) | **PUT** /organizations/{organization}/options | Update options for an organization.
*AdminApi* | [**create_user**](docs/AdminApi.md#create_user) | **POST** /users | Register new user.
*AdminApi* | [**delete_membership**](docs/AdminApi.md#delete_membership) | **DELETE** /organizations/{organization}/memberships/{email} | Remove a user from an organization.
*AdminApi* | [**get_membership**](docs/AdminApi.md#get_membership) | **GET** /organizations/{organization}/memberships/{email} | Get information about organization membership of a rokka user.
*AdminApi* | [**get_organization**](docs/AdminApi.md#get_organization) | **GET** /organizations/{organization} | Get information about an organization.
*SourceimagesApi* | [**copy_source_image**](docs/SourceimagesApi.md#copy_source_image) | **POST** /sourceimages/{organization}/{hash}/copy | Copy a single source image to another org.
*SourceimagesApi* | [**create_source_image**](docs/SourceimagesApi.md#create_source_image) | **POST** /sourceimages/{organization} | Upload new source images.
*SourceimagesApi* | [**create_source_image_meta_dynamic_with_name**](docs/SourceimagesApi.md#create_source_image_meta_dynamic_with_name) | **PUT** /sourceimages/{organization}/{hash}/meta/dynamic/{metaName} | Adds or updates a specific dynamic meta data for an image.
*SourceimagesApi* | [**create_source_image_meta_user**](docs/SourceimagesApi.md#create_source_image_meta_user) | **PUT** /sourceimages/{organization}/{hash}/meta/user | Replace the image meta data with new information.
*SourceimagesApi* | [**create_source_image_meta_user_wth_name**](docs/SourceimagesApi.md#create_source_image_meta_user_wth_name) | **PUT** /sourceimages/{organization}/{hash}/meta/user/{metaName} | Adds or updates one user meta data field for an image.
*SourceimagesApi* | [**delete_source_image**](docs/SourceimagesApi.md#delete_source_image) | **DELETE** /sourceimages/{organization}/{hash} | Delete a single source image.
*SourceimagesApi* | [**delete_source_image_meta_dynamic_with_name**](docs/SourceimagesApi.md#delete_source_image_meta_dynamic_with_name) | **DELETE** /sourceimages/{organization}/{hash}/meta/dynamic/{metaName} | Deletes a specific dynamic meta data.
*SourceimagesApi* | [**delete_source_image_meta_user**](docs/SourceimagesApi.md#delete_source_image_meta_user) | **DELETE** /sourceimages/{organization}/{hash}/meta/user | Deletes all user meta data.
*SourceimagesApi* | [**delete_source_image_meta_user_with_name**](docs/SourceimagesApi.md#delete_source_image_meta_user_with_name) | **DELETE** /sourceimages/{organization}/{hash}/meta/user/{metaName} | Deletes user meta data for a specified field.
*SourceimagesApi* | [**download_source_image**](docs/SourceimagesApi.md#download_source_image) | **GET** /sourceimages/{organization}/{hash}/download | Download original source image binary.
*SourceimagesApi* | [**get_source_image**](docs/SourceimagesApi.md#get_source_image) | **GET** /sourceimages/{organization}/{hash} | Get information about a source image.
*SourceimagesApi* | [**get_source_image_meta_user**](docs/SourceimagesApi.md#get_source_image_meta_user) | **GET** /sourceimages/{organization}/{hash}/meta/user | Get all user meta data.
*SourceimagesApi* | [**get_source_image_meta_user_with_name**](docs/SourceimagesApi.md#get_source_image_meta_user_with_name) | **GET** /sourceimages/{organization}/{hash}/meta/user/{metaName} | Get user meta for a specific field.
*SourceimagesApi* | [**list_source_images**](docs/SourceimagesApi.md#list_source_images) | **GET** /sourceimages/{organization} | Get all images of an organization, with paging.
*SourceimagesApi* | [**list_source_images_by_binary_hash**](docs/SourceimagesApi.md#list_source_images_by_binary_hash) | **GET** /sourceimages/{organization}/binaryhash/{binaryHash} | Get all images in this organization that match a binaryhash.
*SourceimagesApi* | [**patch_source_image_meta_user**](docs/SourceimagesApi.md#patch_source_image_meta_user) | **PATCH** /sourceimages/{organization}/{hash}/meta/user | Update the specified meta data fields for an image.
*SourceimagesApi* | [**restore_source_image**](docs/SourceimagesApi.md#restore_source_image) | **POST** /sourceimages/{organization}/{hash}/restore | Restore source image including previously set metadata.
*StacksApi* | [**create_stack**](docs/StacksApi.md#create_stack) | **PUT** /stacks/{organization}/{name} | Create a new stack.
*StacksApi* | [**delete_stack**](docs/StacksApi.md#delete_stack) | **DELETE** /stacks/{organization}/{name} | Delete a stack.
*StacksApi* | [**get_stack**](docs/StacksApi.md#get_stack) | **GET** /stacks/{organization}/{name} | Get a single stack.
*StacksApi* | [**list_operations**](docs/StacksApi.md#list_operations) | **GET** /operations | Listing all available operations that can be used in stacks.
*StacksApi* | [**list_stack_options**](docs/StacksApi.md#list_stack_options) | **GET** /stackoptions | List all available options that can be set on stacks.
*StacksApi* | [**list_stacks**](docs/StacksApi.md#list_stacks) | **GET** /stacks/{organization} | Get all stacks of an organization.


## Documentation For Models

 - [ListSourceImagesResponse](docs/ListSourceImagesResponse.md)
 - [ListStacksResponse](docs/ListStacksResponse.md)
 - [Membership](docs/Membership.md)
 - [Organization](docs/Organization.md)
 - [OrganizationDefinition](docs/OrganizationDefinition.md)
 - [OrganizationOptions](docs/OrganizationOptions.md)
 - [Role](docs/Role.md)
 - [SourceImage](docs/SourceImage.md)
 - [Stack](docs/Stack.md)
 - [StackDefinition](docs/StackDefinition.md)
 - [StackExpression](docs/StackExpression.md)
 - [StackExpressionOverrides](docs/StackExpressionOverrides.md)
 - [StackOperation](docs/StackOperation.md)
 - [StackOperationDescription](docs/StackOperationDescription.md)
 - [StackOptions](docs/StackOptions.md)
 - [User](docs/User.md)
 - [UserDefinition](docs/UserDefinition.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: api-key
- **Location**: HTTP header


## Author



