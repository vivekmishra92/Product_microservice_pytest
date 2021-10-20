'''
Added the testData file to have a common place for all the testdata used across the application
'''


class Data():

    # Creates a product in the database
    @staticmethod
    def add_valid_product():
        return [{"id": "id_1", "name": "iphone 10", "description": "apple iphone 10"},
                {"id": "id_2", "name": "iphone 11", "description": "apple iphone 11"},
                {"id": "id_3", "name": "iphone 12", "description": "apple iphone 12"}]

    @staticmethod
    def adding_product_with_existing_id():
        return [{"id": "id_1", "name": "iphone 11", "description": "apple iphone 11"}]

    @staticmethod
    def add_product_with_empty_id():
        return [{"id": "", "name": "iwatch 6", "description": "apple watch 6"}]

    @staticmethod
    def add_product_with_special_char_id():
        return [{"id": "@#!", "name": "iwatch 6", "description": "apple watch 6"}]

    @staticmethod
    def add_product_with_empty_product_name():
        return [{"id": "id_4", "name": "", "description": "apple watch 6"}]

    @staticmethod
    def add_product_with_invalid_product_name():
        return [{"id": "id_5", "name": 123 , "description": ""}]

    @staticmethod
    def add_product_with_empty_product_description():
        return [{"id": "id_5", "name": "airpods", "description": ""}]

    # Get a single product by id
    @staticmethod
    def get_product_by_valid_ids():
        return ["id_1", "id_2", "id_3"]

    @staticmethod
    def get_product_by_invalid_ids():
        return ["id_121"]

    #Update a product in the database
    @staticmethod
    def valid_id_for_update():
        return ["id_1"]

    @staticmethod
    def updated_value():
        return [{"id": "id_1", "name": "macbook pro", "description": "apple macbook pro"}]

    @staticmethod
    def invalid_id_for_update():
        return ["id_1234"]

    @staticmethod
    def update_with_empty_name_description():
        return [{"id": "id_1", "name": "", "description": ""}]

    #delete the product in database
    @staticmethod
    def delete_valid_product():
        return ["id_1"]

    @staticmethod
    def delete_nonexisting_product():
        return ["id_1234"]






