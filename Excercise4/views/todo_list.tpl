<html>
  <head>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons+Outlined"rel="stylesheet">
  </head>
<style>
table{border:solid;}
tr{border:solid;}
th{border:solid;}
td{border:solid;}
</style>
<body>
<table >
  <tr>
    <th>ID</th>
    <th>Task</th>
    <th>Completed</th>
    
    
    <th>Delete?</th>
    <th>Description</th>
  </tr>
  %for item in data:
    <tr>
      <th>{{item['id']}}</th>
      <td>{{item['task']}}</td>
      <td>
      %if item['done']:
        <span class="material-icons-outlined">check_circle</span>
      %else:
        <span class="material-icons-outlined">unpublished</span>
      %end
      </td>
     
      <td><a href="/delete/{{item['id']}}"><span class="material-icons">
        delete
        </span></a></td>
      <td><a href="/edit/{{item['id']}}"><span class="material-icons-outlined">
        edit
        </span></a></td>
      </tr>
      
     
      
      </tr>
  %end
</table>
<hr/>
<a href="insert">Add a new task...</a>
<hr/>
</body>
</html>