# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

import requests
import json

import logging
_logger = logging.getLogger(__name__)

_url = "http://localhost:8069/supplier"
_headers = {"Content-Type": "application/json"}


class SupplierTest(TransactionCase):
    # create testing
    def test_create_supplier(self):
        body = {
            "name": "Supplier Test"
        }
        data = json.dumps(body)
        response = requests.post(
            url=_url,
            headers=_headers,
            data=data
        )
        _logger.info(response.json())
        assert response.status_code == 201

    def test_create_supplier_empty_name(self):
        body = {
            "name": ""
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
    def test_get_suppliers(self):
        response = requests.get(
            url=_url,
        )
        _logger.info(response.json())
        assert response.status_code == 200

    # this test below is not activate cause data testing already created
    # just activate if you have deleted all suppliers record in database
    # def test_get_suppliers_not_found(self):
    #     response = requests.get(
    #         url=_url,
    #     )
    #     _logger.info(response.json())
    #     assert response.status_code == 404