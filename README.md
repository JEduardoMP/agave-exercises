## API Implementation

1. Using Flask or Django (preferably Flask), implement a RESTful API with a `POST` endpoint named `/shopping-statistics/category` that takes the following shopping receipt data and returns the total of money spent grouped by category.

    ### Request data:
    ```
    [
        {
            "code": "01827395",
            "name": "Bread",
            "category": "Food",
            "price": 5.30,
            "quantity": 2,
            "percentage_discount": 0
        },
        {
            "code": "17283640",
            "name": "Milk",
            "category": "Food",
            "price": 2.15,
            "quantity": 4,
            "percentage_discount": 10
        },
        {
            "code": "64902891",
            "name": "Computer mouse",
            "category": "Electronics",
            "price": 9.99,
            "quantity": 1,
            "percentage_discount": 15
        },
        {
            "code": "92730769",
            "name": "Soap",
            "category": "Personal hygiene",
            "price": 0.50,
            "quantity": 4,
            "percentage_discount": 7
        },
        {
            "code": "64729981",
            "name": "Pen",
            "category": "Office",
            "price": 0.25,
            "quantity": 10,
            "percentage_discount": 5
        },
        {
            "code": "86009275",
            "name": "Computer keyboard",
            "category": "Electronics",
            "price": 24.99,
            "quantity": 1,
            "percentage_discount": 12
        },
        {
            "code": "95741182",
            "name": "Toilet paper",
            "category": "Personal hygiene",
            "price": 3.15,
            "quantity": 2,
            "percentage_discount": 0.0
        },
        {
            "code": "95017233",
            "name": "Copier paper",
            "category": "Office",
            "price": 3.00,
            "quantity": 10,
            "percentage_discount": 30
        }
    ]
    ```

    ### Response format:
    ```
    {
        "cateogry": 0.00,
        ...
    }
    ```

2. Create one unit test for the implemented endpoint.

3. Add any relevant information and instructions to run the application and test in the `README.md` file inside the directory.

# 

## Refactoring

1. Without using any lint, refactor `refactor_me.py`. Change ANYTHING that you think would be an improvement over the original code.

2. Add any reasoning or relevant information to the `README.md`.
