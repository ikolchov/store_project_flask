# Flask Store Project

The idea is of a store that has employees responsible for adding data and keeping existing products up to date.
There is also a user side to purchase items and share their opinion of a particular item.
There are also few other features.

Following endpoints are available:
----

```
'/register/'
```

- post - Users can register to use other features of the website.

```
'/login/'
```

- post - User gets authenticated with JWT

```
'/administration/'
```

- post - New employees can be registered by the Owners and Managers.
  Upon creation the new employee receives a mail with the password and credentials not available for the user registering
  it. Username is generated based on first/last name.
- put - more product groups can be added to the worker/self if needed by Owner/Manger and Senior.

```
'/employee_login/'
```

- post - Endpoint to log all staff members from the organisation.

```
'/change_password/'
```

- put - Employees and Staff can change their password.
- get - Employees and Staff can reset password and will receive an email with newly generated one.

```
'/store_data_platform/'
```

- put - Employees can insert new products in the DB, the time and user id are logged in the DB.
- get - Employees can get products based on request.
- delete - workers and seniors can delete items from the DB by changing status/ logged in the DB. Owners and managers
  can delete the item from the DB.
- update - Change item values based on criteria, logged in the DB

```
/product_review/<int:id>/'
```

- put - Users can add reviews on a specified item.
- get - Users can decide how many of the most liked comments they would like to see.

```
'/administration/price/'
```

- put - Owners, Managers and Seniors can create discounts for a certain time stamp.
- get - Employees can get all items currently on discount.

```
'/purchase_products/'
```

- get - Users can purchase many products, discount is taken into consideration.

```
'/administration/report/'
```

- get - Only available for Owners. The owner selects a times stamp, after that .xlsx file is uploaded to a specific
  DropBox location that is shared with sales team to analise the data.
  - sheet "top selling' - displays brands by category for that time range
  - sheet "summary" - displays the day the item is sold with other useful information.


### Unit testing for a part of the logic is also implemented.

