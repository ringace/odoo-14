# ODOO 14 
## SUPPLIER & MATERIAL MODULE
### DESCRIPTION
Create addons name supplier and material for material registration needed
### ERD
Entity relationship diagram can be seen on the link below
```sh
https://github.com/ringace/odoo-14/blob/master/documents/ERD.md
```
### INSTALLATION & SETUP
Please following `step by step below`. Installation and setup use `docker`

Clone this repository into your local.
```sh
git@github.com:ringace/odoo-14.git
```
Go to odoo-14 directory
```sh
cd odoo-14
```
Run odoo-14 service, this command will install `odoo 14 framework` and `postgres`
```sh
make up
```
Initialize database, user and password. this command will create database name `odoo14`, user `odoo`, password `odoo`
```sh
make init
```
Install modules or addons. this command will install all base modules and supplier also material modules
```sh
make modules
```

## Test The Service
Testing using odoo test feature
```sh
make tests
```
Here result from odoo test feature
```sh
2024-06-13 21:31:36,749 35 INFO odoo14 odoo.modules.loading: Loading module supplier (2/9) 
2024-06-13 21:31:36,783 35 INFO odoo14 odoo.modules.registry: module supplier: creating or updating database tables 
2024-06-13 21:31:36,864 35 INFO odoo14 odoo.modules.loading: loading supplier/security/ir.model.access.csv 
2024-06-13 21:31:36,885 35 INFO odoo14 odoo.modules.loading: loading supplier/views/supplier_view.xml 
2024-06-13 21:31:36,904 35 INFO odoo14 odoo.modules.loading: loading supplier/views/supplier_action.xml 
2024-06-13 21:31:36,916 35 INFO odoo14 odoo.modules.loading: loading supplier/views/supplier_menuitem.xml 
2024-06-13 21:31:36,932 35 INFO odoo14 odoo.modules.loading: Module supplier: loading demo 
2024-06-13 21:31:36,944 35 INFO odoo14 odoo.addons.supplier.tests.test_controllers: Starting SupplierTest.test_create_supplier ... 
2024-06-13 21:31:37,902 35 INFO odoo14 odoo.addons.supplier.tests.test_controllers: {'message': 'Supplier has been created successfully', 'data': {'id': 1, 'name': 'Supplier Test'}} 
2024-06-13 21:31:37,925 35 INFO odoo14 odoo.addons.supplier.tests.test_controllers: Starting SupplierTest.test_create_supplier_empty_name ... 
2024-06-13 21:31:37,952 35 INFO odoo14 odoo.addons.supplier.tests.test_controllers: {'message': 'Name can not be empty'} 
2024-06-13 21:31:37,953 35 INFO odoo14 odoo.addons.supplier.tests.test_controllers: Starting SupplierTest.test_get_suppliers ... 
2024-06-13 21:31:37,983 35 INFO odoo14 odoo.addons.supplier.tests.test_controllers: {'data': [{'id': 1, 'name': 'Supplier Test'}]} 
2024-06-13 21:31:38,007 35 INFO odoo14 odoo.modules.loading: Module supplier loaded in 1.26s (incl. 1.04s test), 109 queries (+2 test) 
2024-06-13 21:31:38,050 35 INFO odoo14 odoo.modules.loading: Loading module material (6/9) 
2024-06-13 21:31:38,210 35 INFO odoo14 odoo.modules.registry: module material: creating or updating database tables 
2024-06-13 21:31:38,255 35 INFO odoo14 odoo.modules.loading: loading material/security/ir.model.access.csv 
2024-06-13 21:31:38,278 35 INFO odoo14 odoo.modules.loading: loading material/views/material_view.xml 
2024-06-13 21:31:38,295 35 INFO odoo14 odoo.modules.loading: loading material/views/material_action.xml 
2024-06-13 21:31:38,309 35 INFO odoo14 odoo.modules.loading: loading material/views/material_menuitem.xml 
2024-06-13 21:31:38,327 35 INFO odoo14 odoo.modules.loading: Module material: loading demo 
2024-06-13 21:31:38,350 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material ... 
2024-06-13 21:31:38,389 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material has been created successfully', 'data': {'id': 1, 'code': 'T24', 'name': 'test24', 'material_type': 'cotton', 'buy_price': 111.0, 'supplier_id': 1, 'supplier_name': 'Supplier Test'}} 
2024-06-13 21:31:38,412 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_code_unique_effect ... 
2024-06-13 21:31:38,447 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'code': 200, 'message': 'Odoo Server Error', 'data': {'name': 'builtins.TypeError', 'debug': 'Traceback (most recent call last):\n  File "/usr/lib/python3/dist-packages/odoo/addons/base/models/ir_http.py", line 237, in _dispatch\n    result = request.dispatch()\n  File "/usr/lib/python3/dist-packages/odoo/http.py", line 710, in dispatch\n    return self._json_response(result)\n  File "/mnt/extra-addons/material/controllers/controllers.py", line 19, in _alternative_json_response\n    body = json.dumps(response)\n  File "/usr/lib/python3.7/json/__init__.py", line 231, in dumps\n    return _default_encoder.encode(obj)\n  File "/usr/lib/python3.7/json/encoder.py", line 199, in encode\n    chunks = self.iterencode(o, _one_shot=True)\n  File "/usr/lib/python3.7/json/encoder.py", line 257, in iterencode\n    return _iterencode(o, 0)\n  File "/usr/lib/python3.7/json/encoder.py", line 179, in default\n    raise TypeError(f\'Object of type {o.__class__.__name__} \'\nException\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/usr/lib/python3/dist-packages/odoo/http.py", line 652, in _handle_exception\n    return super(JsonRequest, self)._handle_exception(exception)\n  File "/usr/lib/python3/dist-packages/odoo/http.py", line 317, in _handle_exception\n    raise exception.with_traceback(None) from new_cause\nTypeError: Object of type IntegrityError is not JSON serializable\n', 'message': 'Object of type IntegrityError is not JSON serializable', 'arguments': ['Object of type IntegrityError is not JSON serializable'], 'context': {}}} 
2024-06-13 21:31:38,448 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_empty_code ... 
2024-06-13 21:31:38,482 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Code can not be empty'} 
2024-06-13 21:31:38,482 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_empty_material_type ... 
2024-06-13 21:31:38,513 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material type can not be empty'} 
2024-06-13 21:31:38,514 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_empty_name ... 
2024-06-13 21:31:38,545 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Name can not be empty'} 
2024-06-13 21:31:38,546 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_wrong_buy_price_amount ... 
2024-06-13 21:31:38,578 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Buy price must be greater than equal to 100'} 
2024-06-13 21:31:38,579 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_wrong_buy_price_format ... 
2024-06-13 21:31:38,612 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Buy price can not filled by string'} 
2024-06-13 21:31:38,613 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_wrong_material_type ... 
2024-06-13 21:31:38,645 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material type can only be fabric, jeans or cotton'} 
2024-06-13 21:31:38,646 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_wrong_supplier_id_format ... 
2024-06-13 21:31:38,681 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Supplier ID must be integer'} 
2024-06-13 21:31:38,682 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_create_material_wrong_supplier_id_value ... 
2024-06-13 21:31:38,714 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Supplier ID must be greater than equal to 1'} 
2024-06-13 21:31:38,715 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_delete_material_by_id_not_found ... 
2024-06-13 21:31:38,747 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'No material found'} 
2024-06-13 21:31:38,748 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_material_by_id ... 
2024-06-13 21:31:38,786 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'data': {'id': 1, 'code': 'T24', 'name': 'test24', 'material_type': 'cotton', 'buy_price': 111.0, 'supplier_id': 1, 'supplier_name': 'Supplier Test'}} 
2024-06-13 21:31:38,787 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_material_by_id_not_found ... 
2024-06-13 21:31:38,818 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'No material found'} 
2024-06-13 21:31:38,819 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_materials ... 
2024-06-13 21:31:38,854 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'data': [{'id': 1, 'code': 'T24', 'name': 'test24', 'material_type': 'cotton', 'buy_price': 111.0, 'supplier_id': 1, 'supplier_name': 'Supplier Test'}]} 
2024-06-13 21:31:38,855 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_materials_by_type ... 
2024-06-13 21:31:38,889 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'data': [{'id': 1, 'code': 'T24', 'name': 'test24', 'material_type': 'cotton', 'buy_price': 111.0, 'supplier_id': 1, 'supplier_name': 'Supplier Test'}]} 
2024-06-13 21:31:38,890 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_materials_by_type_empty_value ... 
2024-06-13 21:31:38,920 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Empty value request is not allowed, please refer to this example: fabric,jeans,cotton'} 
2024-06-13 21:31:38,921 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_materials_by_type_not_found ... 
2024-06-13 21:31:38,955 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'No material found'} 
2024-06-13 21:31:38,955 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_materials_by_type_spaces_effect ... 
2024-06-13 21:31:38,991 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Whitespace or blank spaces is not allowed, please refer to this example: fabric,jeans,cotton'} 
2024-06-13 21:31:38,992 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_get_materials_by_type_wrong_value ... 
2024-06-13 21:31:39,030 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material type can only be fabric, jeans or cotton'} 
2024-06-13 21:31:39,031 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id ... 
2024-06-13 21:31:39,074 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material has been update successfully', 'data': {'id': 1, 'code': 'T25', 'name': 'test25', 'material_type': 'cotton', 'buy_price': 1000.11, 'supplier_id': 1, 'supplier_name': 'Supplier Test'}} 
2024-06-13 21:31:39,075 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_empty_code ... 
2024-06-13 21:31:39,113 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Code can not be empty'} 
2024-06-13 21:31:39,114 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_empty_material_type ... 
2024-06-13 21:31:39,151 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material type can not be empty'} 
2024-06-13 21:31:39,152 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_empty_name ... 
2024-06-13 21:31:39,187 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Name can not be empty'} 
2024-06-13 21:31:39,188 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_not_found ... 
2024-06-13 21:31:39,222 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'No material found'} 
2024-06-13 21:31:39,223 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_wrong_buy_price_format ... 
2024-06-13 21:31:39,255 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Buy price can not filled by string'} 
2024-06-13 21:31:39,256 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_wrong_by_price_amount ... 
2024-06-13 21:31:39,288 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Buy price must be greater than equal to 100'} 
2024-06-13 21:31:39,289 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_wrong_material_type ... 
2024-06-13 21:31:39,324 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Material type can only be fabric, jeans or cotton'} 
2024-06-13 21:31:39,324 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_wrong_supplier_id_format ... 
2024-06-13 21:31:39,363 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Supplier ID must be integer'} 
2024-06-13 21:31:39,364 35 INFO odoo14 odoo.addons.material.tests.test_controllers: Starting MaterialTest.test_update_material_by_id_wrong_supplier_id_value ... 
2024-06-13 21:31:39,402 35 INFO odoo14 odoo.addons.material.tests.test_controllers: {'message': 'Supplier ID must be greater than equal to 1'} 
2024-06-13 21:31:39,436 35 INFO odoo14 odoo.modules.loading: Module material loaded in 1.39s (incl. 1.05s test), 114 queries (+2 test) 
2024-06-13 21:31:39,476 35 INFO odoo14 odoo.modules.loading: 9 modules loaded in 2.73s, 223 queries (+4 extra) 
2024-06-13 21:31:39,671 35 INFO odoo14 odoo.modules.registry: verifying fields for every extended model 
2024-06-13 21:31:39,868 35 INFO odoo14 odoo.modules.loading: Modules loaded. 
2024-06-13 21:31:39,876 35 INFO odoo14 odoo.service.server: Starting post tests 
2024-06-13 21:31:39,880 35 INFO odoo14 odoo.service.server: 0 post-tests in 0.00s, 0 queries 
2024-06-13 21:31:39,881 35 INFO odoo14 odoo.tests.runner: 0 failed, 0 error(s) of 32 tests when loading database 'odoo14'
```
Testing can be done using tools like `postman`, `insomnia`, `etc`. you can see the document on the link below.
```sh
https://github.com/ringace/odoo-14/blob/master/documents/API.md
```