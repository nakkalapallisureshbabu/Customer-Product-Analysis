<!-- product_details.tpl -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ product['name'] }} Details</title>
</head>
<body>
    <h1>{{ product['name'] }} Details</h1>
    <p>Name: {{ product['name'] }}</p>
    <p>Price: ${{ product['price'] }}</p>
    <p>Quantity: {{ product['quantity'] }}</p>
    <!-- Add more details if necessary -->
    <a href="/products/{{ product['id'] }}/update">Update Product</a>
    <a href="/products/{{ product['id'] }}/delete">Delete Product</a>
    <a href="/products">Back to Products</a>
</body>
</html>
