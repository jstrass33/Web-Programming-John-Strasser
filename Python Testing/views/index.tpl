<html>
  
    <head>
      <title>Smucker's Interface Info</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
  
<style>
table{border:solid;}
tr{border:solid;}
th{border:solid;}
td{border:solid;}
</style>
<body>
<h1 style="text-align: center;">Smucker's Switch Info App</h1>
<br/>
<form action="/" method="post" style="text-align: center;">
  <div class="form-group">
    <label >Enter the username of the Switch:</label>
    <br/>
    <input type="text" name="username" id="username" />
  
    <br/>
  
    <label>Enter the password of the Switch:</label>
    <br/>
    <input type="password" name="password" id="password" />
  
    <br/>
    
    <label>Enter the IP Address of the Switch:</label>
    <br/>
    <input type="text" name="IP" id="IP" />
    <br/>
  
  <div class="form-group form-check"></div>
    <input type="submit" name="submit" id="submit" class="btn btn-primary" value="Get Switch Info"/>
</div>

</form>
</body>
</html>