# coding: utf-8

"""
    rokka.io

    digital image processing done right. [Documentation](https://rokka.io/documentation). [Changelog](https://api.rokka.io/changelog.md).  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import rokka_client_codegen
from rokka_client_codegen.api.sourceimages_api import SourceimagesApi  # noqa: E501
from rokka_client_codegen.rest import ApiException


class TestSourceimagesApi(unittest.TestCase):
    """SourceimagesApi unit test stubs"""

    def setUp(self):
        self.api = rokka_client_codegen.api.sourceimages_api.SourceimagesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_source_image(self):
        """Test case for create_source_image

        Upload new source images.  # noqa: E501
        """
        pass

    def test_create_source_image_meta_dynamic_with_name(self):
        """Test case for create_source_image_meta_dynamic_with_name

        Adds or updates a specific dynamic meta data for an image.  # noqa: E501
        """
        pass

    def test_create_source_image_meta_user(self):
        """Test case for create_source_image_meta_user

        Replace the image meta data with new information.  # noqa: E501
        """
        pass

    def test_create_source_image_meta_user_wth_name(self):
        """Test case for create_source_image_meta_user_wth_name

        Adds or updates one user meta data field for an image.  # noqa: E501
        """
        pass

    def test_delete_source_image(self):
        """Test case for delete_source_image

        Delete a single source image.  # noqa: E501
        """
        pass

    def test_delete_source_image_meta_dynamic_with_name(self):
        """Test case for delete_source_image_meta_dynamic_with_name

        Deletes a specific dynamic meta data.  # noqa: E501
        """
        pass

    def test_delete_source_image_meta_user(self):
        """Test case for delete_source_image_meta_user

        Deletes all user meta data.  # noqa: E501
        """
        pass

    def test_delete_source_image_meta_user_with_name(self):
        """Test case for delete_source_image_meta_user_with_name

        Deletes user meta data for a specified field.  # noqa: E501
        """
        pass

    def test_download_source_image(self):
        """Test case for download_source_image

        Download original source image binary.  # noqa: E501
        """
        pass

    def test_get_source_image(self):
        """Test case for get_source_image

        Get information about a source image.  # noqa: E501
        """
        pass

    def test_get_source_image_meta_user(self):
        """Test case for get_source_image_meta_user

        Get all user meta data.  # noqa: E501
        """
        pass

    def test_get_source_image_meta_user_with_name(self):
        """Test case for get_source_image_meta_user_with_name

        Get user meta for a specific field.  # noqa: E501
        """
        pass

    def test_list_source_images(self):
        """Test case for list_source_images

        Get all images of an organization, with paging.  # noqa: E501
        """
        pass

    def test_list_source_images_by_binary_hash(self):
        """Test case for list_source_images_by_binary_hash

        Get all images in this organization that match a binaryhash.  # noqa: E501
        """
        pass

    def test_patch_source_image_meta_user(self):
        """Test case for patch_source_image_meta_user

        Update the specified meta data fields for an image.  # noqa: E501
        """
        pass

    def test_restore_source_image(self):
        """Test case for restore_source_image

        Restore source image including previously set metadata.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()