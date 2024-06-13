# REST API
### BASE URL
```sh
http://localhost:8069
```
### SUPPLIER
------------------------------------------------------------------------------------------
<details>
<summary><code>POST</code> <code><b>/</b></code> <code>supplier</code></summary>

#### DESCRIPTION
```sh
Create a supplier
```
#### REQUEST
> | Headers      |  Body     |
> |-----------|-----------|
> | `Content-Type": "application/json`      |  `{"name": "Supplier 1"}` | 

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `201`         | `{"message": "Supplier has been created successfully", "data": {"id": 3, "name": "Supplier 1"}}`| 
> | `400`         | `{"message": "Name can not be empty"}`|

</details>

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>supplier</code></summary>

#### DESCRIPTION
```sh
Retrieve all suppliers
```

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `200`         | `{"data": [{"id": 1, "name": "Supplier Test"},]}`| 
> | `404`         | `{"message": "No supplier found"}`|

</details>

### MATERIAL
------------------------------------------------------------------------------------------
<details>
<summary><code>POST</code> <code><b>/</b></code> <code>material</code></summary>

#### DESCRIPTION
```sh
Create a material
```
#### REQUEST
> | Headers      |  Body     |
> |-----------|-----------|
> | `Content-Type": "application/json`      |  `{"code": "M1", "name": "material 1", material_type": "cotton", "buy_price": 1005, "supplier_id": 1}` | 

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `201`         | `{"message": "Material has been created successfully", "data": {"id": 5, "code": "M1", "name": "material 1", "material_type": "cotton", "buy_price": 1005.0, "supplier_id": 1, "supplier_name": "Supplier Test"}}`| 
> | `400`         | `{"message": "Code can not be empty"}`|
> | `400`         | `{"message": "Name can not be empty"}`|
> | `400`         | `{"message": "Material type can not be empty"}`|
> | `400`         | `{"message": "Material type can only be fabric, jeans or cotton"}`|
> | `400`         | `{"message": "Buy price can not filled by string"}`|
> | `400`         | `{"message": "Buy price must be greater than equal to 100"}`|
> | `400`         | `{"message": "Supplier ID must be integer"}`|
> | `400`         | `{"message": "Supplier ID must be greater than equal to 1"}`|

</details>

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>material</code></summary>

#### DESCRIPTION
```sh
Retrieve all materials, can be filtered by material type
```
#### Params
> | Params      |  Value     |
> |-----------|-----------|
> | `type`      |  `fabric,cotton,jeans` for multiple values; `fabric` for single values | 

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `200`         | `{"data": [{"id": 1, "code": "T25", "name": "test25", "material_type": "cotton", "buy_price": 1000.11, "supplier_id": 1, "supplier_name": "Supplier Test"},]}`| 
> | `400`         | `{"message": "Whitespace or blank spaces is not allowed, please refer to this example: fabric,jeans,cotton"}`|
> | `400`         | `{"message": "Empty value request is not allowed, please refer to this example: fabric,jeans,cotton"}`|
> | `400`         | `{"message": "Material type can only be fabric, jeans or cotton"}`|
> | `404`         | `{"message": "No material found"}`|

</details>

<details>
<summary><code>GET</code> <code><b>/</b></code> <code>material</code> <code><b>/</b></code> <code>{id}</code></summary>

#### DESCRIPTION
```sh
Retrieve material by id
```

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `200`         | `{"data": {"id": 1, "code": "T25", "name": "test25", "material_type": "cotton", "buy_price": 1000.11, "supplier_id": 1, "supplier_name": "Supplier Test"}}`| 
> | `404`         | `{"message": "No material found"}`|

</details>

<details>
<summary><code>PUT</code> <code><b>/</b></code> <code>material</code> <code><b>/</b></code> <code>{id}</code></summary>

#### DESCRIPTION
```sh
Update material by id
```
#### REQUEST
> | Headers      |  Body     |
> |-----------|-----------|
> | `Content-Type": "application/json`      |  `{"code": "M2", "name": "material 2", material_type": "cotton", "buy_price": 1005, "supplier_id": 1}` | 

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `200`         | `{"message": "Material has been updated successfully", "data": {"id": 5, "code": "M2", "name": "material 2", "material_type": "cotton", "buy_price": 1005.0, "supplier_id": 1, "supplier_name": "Supplier Test"}}`| 
> | `404`         | `{"message": "No material found"}`|
> | `400`         | `{"message": "Code can not be empty"}`|
> | `400`         | `{"message": "Name can not be empty"}`|
> | `400`         | `{"message": "Material type can not be empty"}`|
> | `400`         | `{"message": "Material type can only be fabric, jeans or cotton"}`|
> | `400`         | `{"message": "Buy price can not filled by string"}`|
> | `400`         | `{"message": "Buy price must be greater than equal to 100"}`|
> | `400`         | `{"message": "Supplier ID must be integer"}`|
> | `400`         | `{"message": "Supplier ID must be greater than equal to 1"}`|

</details>

<details>
<summary><code>DELETE</code> <code><b>/</b></code> <code>material</code> <code><b>/</b></code> <code>{id}</code></summary>

#### DESCRIPTION
```sh
Delete material by id
```

#### Responses
> | Code     | Response                      |
> |---------------|-----------------------------------|
> | `200`         | `{"message": "Material has been deleted successfully"`| 
> | `404`         | `{"message": "No material found"}`|

</details>

