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
Create a material
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