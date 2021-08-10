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
            
            height: 800px;
            width: 800px;
            margin: auto;

            }
        #located{
            height: 75px;
            padding-top: 10px;
        }
    </style>
   <script
   src="https://maps.googleapis.com/maps/api/js?key=     #removed API key for security reasons.                     &callback=initMap&libraries=&v=weekly&channel=2"
   async
   ></script>
    
<script>
      let map;
        
        

        function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 39.056198 , lng: -95.695312 },
            zoom: 4,
            });
        
        google.maps.event.addDomListener(document.getElementById('yosemite'), 'click', function () {

            map.setCenter(new google.maps.LatLng(37.865101,-119.538330));
            map.setZoom(8);
                });
            
        
            google.maps.event.addDomListener(document.getElementById('banff'), 'click', function () {

            map.setCenter(new google.maps.LatLng(51.180202,-115.565704));
            map.setZoom(8);
            });
            

            google.maps.event.addDomListener(document.getElementById('northcascades'), 'click', function () {

            map.setCenter(new google.maps.LatLng(48.6999972 ,-121.1999992));
            map.setZoom(8);
            });

            google.maps.event.addDomListener(document.getElementById('olympic'), 'click', function () {

            map.setCenter(new google.maps.LatLng(47.802109 ,-123.604355));
            map.setZoom(8);
            });

            }

</script>
</head>
<body>
    %include banner
    <div id ="located" class="jumbotron" style="background-color: gold;"> 
        
          <h1 style="text-align: center; color: black;">Where are these Park's  Located?</h1>

    </div>
    <div style="text-align: center;">
    <input id="yosemite" type="button" value="Show Yosemite" class="btn btn-secondary" onclick="" style="margin:0"/>

    <input id="banff" type="button" value="Show Banff" class="btn btn-secondary" onclick="" style="margin:0"/>

    <input id="northcascades" type="button" value="Show North Cascades" class="btn btn-secondary" onclick="" style="margin:0"/>

    <input id="olympic" type="button" value="Show Olympic" class="btn btn-secondary" onclick="" style="margin:0"/>

    </div>
    <br>

    <div>
        
    <div id="map"></div>
    </div>
    
    
    
    
<br>

<br>

<br>

<br>

<br>







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
