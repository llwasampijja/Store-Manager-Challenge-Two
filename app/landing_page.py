webpage = """
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css" type="text/css">
        <style>
            * {
    padding: 0px;
    margin: 0px;
}

html {
    background-color:#BDB76B;
    padding: 0;
    
}

body {
	width:95%;
	max-width:900px;
	margin:0px auto;
	background-color:#FFF;
	overflow:auto;
}

header {
    width: 100%;
    text-align: center;
    background-color: #333300;
    padding-top: 20px;
    padding-bottom: 20px;
}

h1 {
    color: #FFF;
}
nav { 
    width: 300px;
    margin: auto;
}

li {
    list-style: none;
    background-color: #000080;
    padding: 20px 0px;
    margin-top: 10px;
    color: white;
    text-align: center;
    text-emphasis: bold;
    font-family: 'Courier New', Courier, monospace;
    letter-spacing: 3px;
    font-weight: bold;
}

li:hover {
    background-color: #5A7CC2;
}

a {
    text-decoration: none;
	color: #FFF;
}
        </style>
    </head>
    <body>
        <header>
            <h1>Store Manager API Endpoints</h1>
        </header>
        <nav>
            <ul>
                <li> <a href='/api/v1/products'>Get all products</a></li>
                <li> <a href='/api/v1/products/4'>Get a product by id, say id = 4</a></li>
                <li> <a href='/api/v1/products/add'>Add a product</a></li>
                <li> <a href='/api/v1/sales/add'>Create A Sale Order</a></li>
                <li> <a href='/api/v1/sales/2'>Get a Sale Order by id, say id = 2</a></li>
                <li> <a href='/api/v1/sales'>View All Sale Orders</a></li>
            </ul>
        </nav>
    </body>
</html>
"""