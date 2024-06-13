# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

import requests
import json

import logging
_logger = logging.getLogger(__name__)

_url = "http://localhost:8069/material"
_headers = {"Content-Type": "application/json"}


class MaterialTest(TransactionCase):
    # create testing
    def test_create_material(self):
        body = {
            
            "code": "T24",
            "name": "test24",
            "material_type": "cotton",
            "buy_price": 111,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data
        )
        _logger.info(response.json())
        assert response.status_code == 201

    def test_create_material_code_unique_effect(self):
        body = {
            
            "code": "T24",
            "name": "test24",
            "material_type": "cotton",
            "buy_price": 111,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data
        )
        _logger.info(response.json())
        assert response.status_code == 500

    def test_create_material_empty_code(self):
        body = {
            
            "code": "",
            "name": "test23",
            "material_type": "cotton",
            "buy_price": 111,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_empty_name(self):
        body = {
            
            "code": "T23",
            "name": "",
            "material_type": "cotton",
            "buy_price": 111,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_empty_material_type(self):
        body = {
            
            "code": "T23",
            "name": "test23",
            "material_type": "",
            "buy_price": 111,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_wrong_material_type(self):
        body = {
            
            "code": "T23",
            "name": "test23",
            "material_type": "leather",
            "buy_price": 111,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_wrong_buy_price_format(self):
        body = {
            
            "code": "T23",
            "name": "test23",
            "material_type": "cotton",
            "buy_price": "",
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_wrong_buy_price_amount(self):
        body = {
            
            "code": "T23",
            "name": "test23",
            "material_type": "cotton",
            "buy_price": 99,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_wrong_supplier_id_format(self):
        body = {
            
            "code": "T23",
            "name": "test23",
            "material_type": "cotton",
            "buy_price": 1100,
            "supplier_id": "1"
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_create_material_wrong_supplier_id_value(self):
        body = {
            
            "code": "T23",
            "name": "test23",
            "material_type": "cotton",
            "buy_price": 1100,
            "supplier_id": 0
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400
    
    # get all testing
    def test_get_materials(self):
        response = requests.get(
            url=_url,
        )
        _logger.info(response.json())
        assert response.status_code == 200

    def test_get_materials_by_type(self):
        params = {"type": "fabric,cotton"}
        response = requests.get(
            url=_url,
            params=params
        )
        _logger.info(response.json())
        assert response.status_code == 200

    def test_get_materials_by_type_spaces_effect(self):
        params = {"type": "      fabric,cotton"}
        response = requests.get(
            url=_url,
            params=params
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_get_materials_by_type_empty_value(self):
        params = {"type": "fabric,,cotton"}
        response = requests.get(
            url=_url,
            params=params
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_get_materials_by_type_wrong_value(self):
        params = {"type": "fabric,leather,cotton"}
        response = requests.get(
            url=_url,
            params=params
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_get_materials_by_type_not_found(self):
        params = {"type": "fabric,jeans"}
        response = requests.get(
            url=_url,
            params=params
        )
        _logger.info(response.json())
        assert response.status_code == 404

    # get specific material testing
    def test_get_material_by_id(self):
        response = requests.get(
            url=f"{_url}/1",
        )
        _logger.info(response.json())
        assert response.status_code == 200

    def test_get_material_by_id_not_found(self):
        response = requests.get(
            url=f"{_url}/1000",
        )
        _logger.info(response.json())
        assert response.status_code == 404

    # update material testing
    def test_update_material_by_id(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": 1000.11,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 200

    def test_update_material_by_id_not_found(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": 1000.11,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1000",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 404

    def test_update_material_by_id_empty_code(self):
        body = {
            
            "code": "",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": 1000.11,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_empty_name(self):
        body = {
            
            "code": "T25",
            "name": "",
            "material_type": "cotton",
            "buy_price": 1000.11,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_empty_material_type(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "",
            "buy_price": 1000.11,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_wrong_material_type(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "leather",
            "buy_price": 1000.11,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_wrong_buy_price_format(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": "",
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_wrong_by_price_amount(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": 70.25,
            "supplier_id": 1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_wrong_supplier_id_format(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": 1000.11,
            "supplier_id": ""
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    def test_update_material_by_id_wrong_supplier_id_value(self):
        body = {
            
            "code": "T25",
            "name": "test25",
            "material_type": "cotton",
            "buy_price": 1000.11,
            "supplier_id": -1
        }
        data = json.dumps(body)
        response = requests.put(
            url=f"{_url}/1",
            headers=_headers,
            data=data,
        )
        _logger.info(response.json())
        assert response.status_code == 400

    # delete material testing
    # this test below is not activate cause will delete data testing
    # just activate if there are more than 1 record in material and change value 1 to another value
    # def test_delete_material_by_id_not_found(self):
    #     response = requests.delete(
    #         url=f"{_url}/1"
    #     )
    #     _logger.info(response.json())
    #     assert response.status_code == 200

    def test_delete_material_by_id_not_found(self):
        response = requests.delete(
            url=f"{_url}/1000"
        )
        _logger.info(response.json())
        assert response.status_code == 404





