<html>
<head>
    %include header
</head>
<body>
    %include banner
<table class="table table-striped table-hover">
  <tr class="thead-dark">
    <th>Hobby</th>
    <th>Years Spent Doing Activity</th>
    <th>Delete?</th>
    
  </tr>
  %for item in items:
    <tr>
      <td>{{item['hobby']}}</td>
      <td>{{item['years']}}</td>
    
        <td><a href="/delete_hobby/{{item['id']}}"><span class="material-icons">delete</span></a> </td>
    </tr>
  %end
</table>
<hr/>
<form action="/midterm" method="post">
    <div class="form-group" style="text-align: center;">
    <label>Add a New Hobby</label>
    <input type="text" name="newhobby" id="newhobby" class="form-control"/>
    </div>
    <div class="form-group" style="text-align: center;">
    <label >Number of Years Doing</label>
    <input type="text" name="years" id="years" class="form-control"/>
    </div>
    <div style="text-align: center;">
    <button type="submit" name="submit" id="submit" class="btn btn-primary" value="Add a New Hobby" onclick="loading()">Add a New Hobby</button>
    </div>
</form>
<hr/>

<button class="btn btn-primary" data-toggle="collapse" data-target="#demo">Show National Park Photography</button>

<div id="demo" class="collapse">
Lorem ipsum dolor text....
    <img src="/static/Yosemite.jpg" />
</div>
</body>

<script>

    function loading(){
      const element = document.getElementById("submit");
      const span = document.createElement("span");
      
      span.classList.add("spinner-border"); 
      span.classList.add("spinner-border-sm"); 
      
      element.innerHTML = "Loading...    ";
      element.appendChild(span);
      
    }
  
  </script>
</html>