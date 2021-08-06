<html>
<head>
    %include header
    <style>

        body{
            background-color: darkgray;
        }
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
        #map {
            height: 100%;
            height: 400px;
            width: 400px;

            }
    </style>
    <script>
        let map;

        function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 48.6999972 , lng: -121.1999992 },
            zoom: 8,
            });
            }
    </script>

    <script
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB41DRUbKWJHPxaFjMAwdrzWzbVKartNGg&callback=initMap&libraries=&v=weekly&channel=2"
    async
    ></script>
</head>
<body>
    %include banner
    
    
    <h3>Olympic National Park Photography</h3> 
    
<h4 id=nationalpark>Scroll Down to the Bottom to Leave a Comment</h4>
</br>
<div class="row">
    
    <div class="col-sm">
        <img src="/static/hurricaneflowers.JPG" alt="Olympic National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/olym/index.htm" target="_blank">Hurricane Ridge - Olympic National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/marymerefalls.JPG" alt="Olympic National Park - Moraine Lake" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/olym/index.htm" target="_blank">Olympic National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/stormking.JPG" alt="North Cascades National Park - Peyton Lake" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/olym/index.htm" target="_blank">Mount Storm King - Olympic National Park</a></figcaption>
    </div>
  </div>
  <div class="row">
    
    <div class="col-sm">
        <img src="/static/rubybeach.jpg" alt="Olympic National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/olym/index.htm" target="_blank">Ruby Beach - Olympic National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/hurricaneridge.jpg" alt="Olympic National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/olym/index.htm" target="_blank">Olympic National Park</a></figcaption>
    </div>
    <div class="col-sm">
        <img src="/static/rainforest.jpg" alt="Olympic National Park" class="img-fluid float-left img-thumbnail"/>
        <figcaption style="text-align: center;"><a href="https://www.nps.gov/olym/index.htm" target="_blank">Olympic National Park</a></figcaption>
    </div>
  </div>
    
</div>

<br>

<br>

<br>



<form action="/comments" method="post" style="text-align: center;">
    <input type="hidden" name="nationalpark" value='olympic' display='None' />
    <!--Username <input type="text" name="username"/><br> <br>-->
    <b>Add Comment </b><br>
    <textarea type="text" name="comment" class='media-body' style="width:800px; margin:0 auto; border-style: groove; margin-bottom: 10px; height: 100px;">Enter a new comment...</textarea><br>
    <hr/>
    <input type="submit" class="btn btn-primary"value="Submit"/>
    </form>

<p style="text-align: center;"><b>{{commentsnumber}} New Comments </b></p>
<hr>

%for item in items:
<div class='media-body' style="width:800px; margin:0 auto; border-style: groove; margin-bottom: 10px; background-color: white;">

    <img src="/static/avatar.png" alt="Avatar" class="float-left"  style="width: 30px; height:30px; padding-left: 5px; padding-top: 5px;"/> 
    <p style="margin-left: 40px; margin-top: 5px;"><b>{{item['username']}}</b> made a comment at <b>{{item['date']}}</b></p>
    
  
  
    
   <p style="padding-left: 75px;">
    {{item['comment']}}
    %if user in item['username']:
    <a href="/delete/{{nationalpark}}/{{item['id']}}" style="float: right; margin-right: 10px;"><span class="material-icons">
        delete
        </span></a>
    </p>

   
   %end

</div>



%end
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