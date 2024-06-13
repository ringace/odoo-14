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
> | `200`         | `{"data": [{"id": 1, "name": "Supplier Test"}]}`| 
> | `404`         | `{"message": "No supplier found"}`|

</details>