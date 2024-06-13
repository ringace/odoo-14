#-*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response, JsonRequest

import json
import re

import logging
_logger = logging.getLogger(__name__)

# function to change jsonrpc response format
def _alternative_json_response(self, result=None, error=None):
    if error is not None:
        response = error
    if result is not None:
        response = result

    headers = {"Content-Type": "application/json"}
    body = json.dumps(response)

    return Response(body, headers=headers)


class Material(http.Controller):
    # create a new material
    @http.route("/material", auth="public", csrf=False, type="json", methods=["POST"])
    def create_material(self):
        # change standard jsonrpc response format
        request._json_response = _alternative_json_response.__get__(request, JsonRequest)

        # get json request
        args = request.httprequest.data.decode()
        values = json.loads(args)

        # code validation
        if not values.get("code"):
            Response.status = "400"
            return {
                "message": "Code can not be empty"
            }

        # name validation
        if not values.get("name"):
            Response.status = "400"
            return {
                "message": "Name can not be empty"
            }

        # material type validation
        if not values.get("material_type"):
            Response.status = "400"
            return {
                "message": "Material type can not be empty"
            }
        if values.get("material_type") not in ["fabric", "jeans", "cotton"]:
            Response.status = "400"
            return {
                "message": "Material type can only be fabric, jeans or cotton"
            }

        # buy price validation
        if isinstance(values.get("buy_price"), str):
            Response.status = "400"
            return {
                "message": "Buy price can not filled by string"
            }
        if values.get("buy_price") < 100:
            Response.status = "400"
            return {
                "message": "Buy price must be greater than equal to 100"
            }

        # supplier validation
        if not isinstance(values.get("supplier_id"), int):
            Response.status = "400"
            return {
                "message": "Supplier ID must be integer"
            }
        if values.get("supplier_id") < 1:
            Response.status = "400"
            return {
                "message": "Supplier ID must be greater than equal to 1"
            }

        try:
            # request saved
            material = request.env["material"].sudo().create(values)
            _logger.info(f"Saved material: {material}")
        except Exception as error:
            # save failed
            Response.status = "500"
            return {
                "message": error
            }

        # set material
        data = {
            "id": material.id,
            "code": material.code,
            "name": material.name,
            "material_type": material.material_type,
            "buy_price": material.buy_price,
            "supplier_id": material.supplier_id.id,
            "supplier_name": material.supplier_id.name,
        }

        # save successful
        Response.status = "201"
        return {
            "message": "Material has been created successfully",
            "data": data
        }
            
    # get all material
    @http.route("/material", auth="public", csrf=False, type="http", methods=["GET"])
    def get_materials(self, **kwargs):
        # set headers
        headers = {"Content-Type": "application/json"}

        # materials_type_allowed
        materials_type_allowed = ["fabric", "cotton", "jeans"]

        # get materials type query parameters
        materials_type_request = kwargs.get("type")

        # set request from query parameters and material_type validation if material type exists
        if materials_type_request:
            # whitespace or spaces not allowed
            if re.search(r"\s+", materials_type_request):
                Response.status = "400"
                return Response(
                    json.dumps({
                        "message": "Whitespace or blank spaces is not allowed, please refer to this example: fabric,jeans,cotton"
                    }),
                    headers=headers
                )
            # make array
            materials_type_request = materials_type_request.split(",")
            # empty string in list not allowed
            if "" in materials_type_request:
                Response.status = "400"
                return Response(
                    json.dumps({
                        "message": "Empty value request is not allowed, please refer to this example: fabric,jeans,cotton"
                    }),
                    headers=headers
                )
            # compare if material request match with material allowed
            materials_compare_result = all(ele in materials_type_allowed for ele in materials_type_request)
            # material type request is not allowed
            if not materials_compare_result:
                Response.status = "400"
                return Response(
                    json.dumps({
                        "message": "Material type can only be fabric, jeans or cotton"
                    }),
                    headers=headers
                )

        try:
            if materials_type_request:
                # get materials by material type
                materials = request.env["material"].sudo().search([("material_type", "in", materials_type_request)])
            else:
                # get all materials
                materials = request.env["material"].sudo().search([])
        except Exception as error:
            # get materials failed
            Response.status = "500"
            return Response(
                json.dumps({
                    "message": error
                }),
                headers=headers
            )
            

        if not materials:
            # no material found
            Response.status = "404"
            return Response(
                json.dumps({
                    "message": "No material found"
                }),
                headers=headers
            )

        # set materials
        data = [
            {
                "id": m.id,
                "code": m.code,
                "name": m.name,
                "material_type": m.material_type,
                "buy_price": m.buy_price,
                "supplier_id": m.supplier_id.id,
                "supplier_name": m.supplier_id.name
            }
            for m in materials
        ]

        # materials retrieved
        Response.status = "200"
        return Response(
            json.dumps({
                "data": data
            }),
            headers=headers
        )

    # get material by id
    @http.route("/material/<int:material_id>", auth="public", csrf=False, type="http", methods=["GET"])
    def get_material_by_id(self, material_id):
        # set headers
        headers = {"Content-Type": "application/json"}  

        try:
            # get material by single id
            material = request.env["material"].sudo().search([("id", "=", material_id)])
        except Exception as error:
            # get material failed
            Response.status = "500"
            return Response(
                json.dumps({
                    "message": error
                }),
                headers=headers
            )
            

        if not material:
            # no material found
            Response.status = "404"
            return Response(
                json.dumps({
                    "message": "No material found"
                }),
                headers=headers
            )

        # set material
        data = {
            "id": material.id,
            "code": material.code,
            "name": material.name,
            "material_type": material.material_type,
            "buy_price": material.buy_price,
            "supplier_id": material.supplier_id.id,
            "supplier_name": material.supplier_id.name
        }

        # material retrieved
        Response.status = "200"
        return Response(
            json.dumps({
                "data": data
            }),
            headers=headers
        )

    # update material by id
    @http.route("/material/<int:material_id>", auth="public", csrf=False, type="json", methods=["PUT"])
    def update_material_by_id(self, material_id):
        # change standar jsonrpc response format
        request._json_response = _alternative_json_response.__get__(request, JsonRequest)

        try:
            # get material by single id
            material = request.env["material"].sudo().search([("id", "=", material_id)])
        except Exception as error:
            # get material failed
            Response.status = "500"
            return {
                "message": error
            }
            

        if not material:
            # no material found
            Response.status = "404"
            return {
                "message": "No material found"
            }

        # get json request
        args = request.httprequest.data.decode()
        values = json.loads(args)

        # code validation
        if not values.get("code"):
            Response.status = "400"
            return {
                "message": "Code can not be empty"
            }

        # name validation
        if not values.get("name"):
            Response.status = "400"
            return {
                "message": "Name can not be empty"
            }

        # material type validation
        if not values.get("material_type"):
            Response.status = "400"
            return {
                "message": "Material type can not be empty"
            }
        if values.get("material_type") not in ["fabric", "jeans", "cotton"]:
            Response.status = "400"
            return {
                "message": "Material type can only be fabric, jeans or cotton"
            }

        # buy price validation
        if isinstance(values.get("buy_price"), str):
            Response.status = "400"
            return {
                "message": "Buy price can not filled by string"
            }
        if values.get("buy_price") < 100:
            Response.status = "400"
            return {
                "message": "Buy price must be greater than equal to 100"
            }

        # supplier validation
        if not isinstance(values.get("supplier_id"), int):
            Response.status = "400"
            return {
                "message": "Supplier ID must be integer"
            }
        if values.get("supplier_id") < 1:
            Response.status = "400"
            return {
                "message": "Supplier ID must be greater than equal to 1"
            }

        try:
            # request updated
            material.write(values)
        except Exception as error:
            # update failed
            Response.status = "500"
            return {
                "message": error
            }

        # set material
        data = {
            "id": material.id,
            "code": material.code,
            "name": material.name,
            "material_type": material.material_type,
            "buy_price": material.buy_price,
            "supplier_id": material.supplier_id.id,
            "supplier_name": material.supplier_id.name
        }

        # material updated
        Response.status = "200"
        return {
            "message": "Material has been update successfully",
            "data": data
        }

    # delete material by id
    @http.route("/material/<int:material_id>", auth="public", csrf=False, type="http", methods=["DELETE"])
    def delete_material_by_id(self, material_id):
        # set headers
        headers = {"Content-Type": "application/json"}  

        try:
            # delete material by single id
            material = request.env["material"].sudo().search([("id", "=", material_id)])
        except Exception as error:
            # get material failed
            Response.status = "500"
            return Response(
                json.dumps({
                    "message": error
                }),
                headers=headers
            )
            

        if not material:
            # no material found
            Response.status = "404"
            return Response(
                json.dumps({
                    "message": "No material found"
                }),
                headers=headers
            )

        try:
            # request deleted
            material.unlink()
        except Exception as error:
            # delete failed
            Response.status = "500"
            return Response(
                json.dumps({
                    "message": error
                }),
                headers=headers
            )

        # material deleted
        Response.status = "200"
        return Response(
            json.dumps({
                "message": "Material has been delete successfully"
            }),
            headers=headers
        )