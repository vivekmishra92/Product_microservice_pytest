from data import Data
import pytest

class TestPostProduct(object):
    '''
        below tests will test the POST Api of the product
        '''
    @pytest.mark.parametrize("data", Data.add_valid_product())
    def test_add_valid_product(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 200
        assert data['id'] != ""
        assert data['name'] != ""
        assert data['description'] != ""
        assert data['_id'] != ""

    #Database should not add new data with product id which is already present in database
    @pytest.mark.parametrize("data", Data.adding_product_with_existing_id())
    def test_adding_product_with_existing_id(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 400
        assert data['err'] != ""

    # Database should not add new data without product id
    @pytest.mark.parametrize("data", Data.add_product_with_empty_id())
    def test_add_product_with_empty_id(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 400
        assert data['err'] != ""

    # Database should not add new data with invalid product id
    @pytest.mark.parametrize("data", Data.add_product_with_special_char_id())
    def test_add_product_with_special_char_id(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 400
        assert data['err'] != ""

    # Database should not add new data with empty product name
    @pytest.mark.parametrize("data", Data.add_product_with_empty_product_name())
    def test_add_product_with_empty_product_name(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 400
        assert data['err'] != ""

    # Database should not add new data with empty product description
    @pytest.mark.parametrize("data", Data.add_product_with_empty_product_description())
    def test_add_product_with_empty_product_description(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 400
        assert data['err'] != ""

    # Database should not add new data with invalid product name
    @pytest.mark.parametrize("data", Data.add_product_with_invalid_product_name())
    def test_add_product_with_invalid_product_name(self, data, testhelper_object):
        status_code, data = testhelper_object.post_product(data)
        assert status_code == 400
        assert data['err'] != ""

    '''
    below tests will test 2 GET api(get all product and get product by id) of the product
    '''
    def test_get_all_product(self, testhelper_object):
        status_code, data = testhelper_object.get_all_product()
        assert status_code == 200
        assert len(data) != 0

    @pytest.mark.parametrize("id", Data.get_product_by_valid_ids())
    def test_get_product_by_id(self, id, testhelper_object):
        status_code, data = testhelper_object.get_product_by_id(id)
        assert status_code == 200
        assert data["id"] == id

    @pytest.mark.parametrize("id", Data.get_product_by_invalid_ids())
    def test_get_product_by_invalid_id(self, id, testhelper_object):
        status_code, data = testhelper_object.get_product_by_id(id)
        assert status_code == 404


    '''
    below tests will test the UPDATE Api of the product
    '''

    @pytest.mark.parametrize("product_id", Data.valid_id_for_update())
    @pytest.mark.parametrize("update_data", Data.updated_value())
    def test_update_the_valid_product(self, product_id, update_data, testhelper_object):
        status_code, data = testhelper_object.update_product(product_id, update_data)
        assert status_code == 200
        assert data["name"] == update_data["name"]
        assert data["description"] == update_data["description"]

    @pytest.mark.parametrize("product_id", Data.invalid_id_for_update())
    @pytest.mark.parametrize("update_data", Data.updated_value())
    def test_update_the_invalid_product_id(self, product_id, update_data, testhelper_object):
        status_code, data = testhelper_object.update_product(product_id, update_data)
        assert status_code == 404

    @pytest.mark.parametrize("product_id", Data.valid_id_for_update())
    @pytest.mark.parametrize("update_data", Data.update_with_empty_name_description())
    def test_update_the_invalid_product_details(self, product_id, update_data, testhelper_object):
        status_code, data = testhelper_object.update_product(product_id, update_data)
        assert status_code == 404

    '''
    below tests will test the Delete Api of the product
    '''

    @pytest.mark.parametrize("product_id", Data.delete_valid_product())
    def test_delete_valid_product(self, product_id, testhelper_object):
        status_code, data = testhelper_object.delete_product(product_id)
        assert status_code == 200
        assert data["ok"] == 1

    @pytest.mark.parametrize("product_id", Data.delete_nonexisting_product())
    def test_delete_product_with_non_existing_product_it(self, product_id, testhelper_object):
        status_code, data = testhelper_object.delete_product(product_id)
        assert status_code == 200
        assert data["ok"] == 0


