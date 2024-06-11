#-*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, Response, JsonRequest

import json

# function to change jsonrpc response format
def _alternative_json_response(self, result=None, error=None):
    if error is not None:
        response = error
    if result is not None:
        response = result

    headers = {"Content-Type": "application/json"}
    body = json.dumps(response)

    return Response(body, headers=headers)


class Supplier(http.Controller):
    # create a new supplier
    @http.route("/supplier", auth="public", csrf=False, type="json", methods=["POST"])
    def create_supplier(self):
        # change standar jsonrpc response format
        request._json_response = _alternative_json_response.__get__(request, JsonRequest)

        # get json request
        args = request.httprequest.data.decode()
        values = json.loads(args)

        # name validation
        if not values.get("name"):
            Response.status = "400"
            return {
                "message": "Name can not be empty"
            }

        try:
            # request saved
            supplier = request.env["supplier"].sudo().create(values)
        except Exception as error:
            # save failed
            Response.status = "500"
            return {
                "message": error
            }

        # set supplier
        data = {
            "id": supplier.id,
            "name": supplier.name
        }

        # save successful
        Response.status = "201"
        return {
            "message": "Supplier has been created successfully",
            "data": data
        }
            
    # get all supplier
    @http.route("/supplier", auth="public", csrf=False, type="http", methods=["GET"])
    def get_suppliers(self):
        # set headers
        headers = {"Content-Type": "application/json"}  

        try:
            # get all suppliers
            suppliers = request.env["supplier"].sudo().search([])
        except Exception as error:
            # get suppliers failed
            Response.status = "500"
            return Response(
                json.dumps({
                    "message": error
                }),
                headers=headers
            )
            

        if not suppliers:
            # no supplier found
            Response.status = "404"
            return Response(
                json.dumps({
                    "message": "No supplier found"
                }),
                headers=headers
            )

        # set suppliers
        data = [
            {
                "id": s.id,
                "name": s.name
            }
            for s in suppliers
        ]

        # suppliers retrieved
        Response.status = "200"
        return Response(
            json.dumps({
                "data": data
            }),
            headers=headers
        )