# Rest-api

## Setup

1. Clone the repository.
2. Install Python 3.9 or greater.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Create a sqllite database and update the `DATABASES` configuration in `settings.py` accordingly.
5. Apply the database migrations by running `python manage.py migrate`.
6. Create a superuser by running `python manage.py createsuperuser`.
7. Run the development server by running `python manage.py runserver`.

## API Documentation

### Authentication

All API endpoints require authentication using Token authentication. You can obtain a token by sending a POST request to the `api-token-auth/` endpoint with a valid username and password in the request body.
Example usage:
POST http://127.0.0.1:8000/api-token-auth/
Add the token generated in the Headers

### Endpoints

#### GET http://127.0.0.1:8000/api/

Returns a list of all products. ex :

[
    {
        "id": 1,
        "name": "TV",
        "description": "good lcd tv",
        "price": "3000.000"
    },
    {
        "id": 2,
        "name": "phone",
        "description": "nice phone",
        "price": "300.000"
    }
]


#### POST  http://127.0.0.1:8000/api/

Creates a new product.

##### Request Body


#### GET /api/{product_id}/

Returns the details of a specific product.

##### 



#### PUT /api/{product_id}/

Updates the details of a specific product.

##### 


#### DELETE /api/{product_id}/

Deletes a specific product.

#####

##### Search
##### GET /api/search/
Returns a list of products that match the specified search query.
Example usage:
    /api/search/?query=phone
#####

##### Pagination
#####  GET /api/search/?query=phone&page=1
Returns a list of products that match the specified search query and page no.
Example usage:
     GET http://127.0.0.1:8000/api/search/?query=phone&page=1


##### Sorting
#####  GET /api/?sort_by=price&sort_order=desc
Returns a list of products that match the specified search query and page no.
Example usage:
     GET http://127.0.0.1:8000/api/?sort_by=price&sort_order=desc

