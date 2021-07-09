<html>
<head>
    %include header
    <style>
        #nationalpark{
            text-align: center;
        }
        h3{
            text-align: center;
        }
        #addhobby{
            
            font-weight: bold;
        }
        
        figcaption{
            font-weight: bold;
        }
        #addyears{
            
            font-weight: bold;
        
        
        }
        #aboutme{background-color: white;

        }
    </style>
</head>
<body>
    %include banner
    
    <div style="background-color: gold;" class="pt-0 my-0">
    <h3>A list of some of my hobbies</h3> 
    </div>
<table class="table table-striped table-hover">
  <tr class="text-white" style="background-color: rgb(77, 94, 248);">
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

<form action="/midterm" method="post">
    <div class="form-group" style="text-align: center;">
    <label id="addhobby">Add a New Hobby:</label>
    <input type="text" name="newhobby" id="newhobby" class="form-control" required/>
    </div>
    <div class="form-group" style="text-align: center;">
    <label id="addyears" >Number of Years Doing:</label>
    <input type="text" name="years" id="years" class="form-control" required/>
    </div>
    <div style="text-align: center;">
    <button type="submit" name="submit" id="submit" class="btn btn-warning" value="Add a New Hobby" onclick="loading()"><strong>Add a New Hobby</strong></button>
    </div>
</form>

<label>Click Button and Scroll Down to See Photos</label>
</br>
<button class="btn btn-primary" data-toggle="collapse" data-target="#demo" id="demo1"><Strong>Show National Park Photography</Strong></button>

<div id="demo" class="collapse">
<h4 id=nationalpark>National Park Photography</h4>
</br>
<div class="row">
    <div class="col-sm">
        <img src="/static/Yosemite.jpg" alt="Yosemite National Park" class="img-fluid float-left img-thumbnail"/> 
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/yose/index.htm" target="_blank">Yosemite National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/moraine lake Sunrise.jpg" alt="Banff National Park - Moraine Lake" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.pc.gc.ca/en/pn-np/ab/banff" target="_blank">Banff National Park - Moraine Lake</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/Peyto Lake.jpg" alt="Banff National Park - Peyton Lake" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.pc.gc.ca/en/pn-np/ab/banff" target="_blank">Banff National Park - Peyto Lake</a></figcaption>
    </div>
  </div>

  <div class="row">
    <div class="col-sm">
        <img src="/static/Skyline Trail.jpg" alt="Jasper National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.pc.gc.ca/en/pn-np/ab/jasper" target="_blank">Jasper National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/sunWapta Falls (2).jpg" alt="Jasper National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.pc.gc.ca/en/pn-np/ab/jasper" target="_blank">Jasper National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/wapta Falls.jpg" alt="Yoho National Park - Wapta Falls" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.pc.gc.ca/en/pn-np/bc/yoho" target="_blank">Yoho National Park - Wapta Falls</a></figcaption>
    </div>
  </div>
    
  <div class="row">
    <div class="col-sm">
        <img src="/static/cirque peak.jpg" alt="Banff National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.pc.gc.ca/en/pn-np/ab/banff" target="_blank">Banff National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/horseshoebend.JPG" alt="Horsehoe Bend " class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://horseshoebend.com/" target="_blank">HorseShoe Bend</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/antelope.JPG" alt="Antelope Canyon" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://en.wikipedia.org/wiki/Antelope_Canyon" target="_blank">Antelope Canyon</a></figcaption>
    </div>
  </div>
    
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