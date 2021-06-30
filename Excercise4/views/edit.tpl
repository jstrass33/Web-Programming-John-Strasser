<html>
<body>
<form action="/edit" method="post">
<input type="text" name="id" value="{{item['id']}}" hidden/>
Edit Task: <input type="text" name="task" value="{{item['task']}}"/><br>
<hr/>
<button onclick="window.location='/'; return false">Cancel</button>&nbsp
<input type="submit" value="Submit"/>
</form>

<hr/>
</body>
</html>