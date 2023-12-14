<!-- customer_details.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ customer['name'] }} Details</title>
</head>
<body>
    <h1>{{ customer['name'] }} Details</h1>
    <p>Name: {{ customer['name'] }}</p>
    <p>Email: {{ customer['email'] }}</p>
    <!-- Add more details if necessary -->
    <a href="/customers/{{ customer['id'] }}/update">Update Customer</a>
    <a href="/customers/{{ customer['id'] }}/delete">Delete Customer</a>
    <a href="/customers">Back to Customers</a>
</body>
</html>
