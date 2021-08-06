<html>
<head>
    %include header
    <style>
        
        .main{
            height: 1200px;

            text-align: center;
            background-image: url("/static/banff.jpg");
            background-size: 100% 100%;
        

        } 
        #transparent{
            background-color: rgba(255,255,255,0.6);
            height: 100%;
        }
        #nav{
            height: 75px;
            background-color: navy;
            color: gold;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        }
        a:hover{
            text-decoration: underline;
            color:white;
        }
        a{
            color:gold;
        }

        .caption{
            background-color: rgba(255,255,255,0.6);
        }
        

    </style>
</head>
<body>
   




    %include banner

  <div id="main" class="jumbotron main"> 
      <div id="transparent">
        <h1 style="padding-top: 25px;">John's Higher Views</h1>
        <h3 style="padding-top: 25px;">Click the Below Photos for Photo Albums from Each National Park</h3>
     
  

        
        
        <div id="demo" class="carousel slide" data-ride="carousel" style="height: 600; width: 900; margin: auto;">

            <!-- Indicators -->
            <ul class="carousel-indicators">
            <li data-target="#demo" data-slide-to="0" class="active"></li>
            <li data-target="#demo" data-slide-to="1"></li>
            <li data-target="#demo" data-slide-to="2"></li>
            </ul>
        
            <!-- The slideshow -->
            <div class="carousel-inner">
            <div class="carousel-item active">
                <a href="/banff"><img src="/static/Peyto Lake.jpg") alt="Los Angeles" class="img-fluid float-left"> </a>
                <div class="carousel-caption caption">
                    <h3 style="color: black; padding-bottom: 20px;">Banff National Park</h3>
                    <p style="color: black;">Click photo to see the full album</p>
                  </div>
            </div>
            <div class="carousel-item">
                <a href="/yosemite"><img src="/static/Yosemite.jpg" alt="Chicago" class="img-fluid float-left"></a>
                <div class="carousel-caption caption">
                    <h3 style="color: black; padding-bottom: 20px;">Yosemite National Park</h3>
                    <p style="color: black;">Click photo to see the full album</p>
                  </div>
            </div>
            <div class="carousel-item">
               <a href="/northcascades"> <img src="/static/hiddenlake.JPG" alt="New York" class="img-fluid float-left"></a>
                <div class="carousel-caption caption">
                    <h3 style="color: black; padding-bottom: 20px;">North Cascades National Park</h3>
                    <p style="color: black;">Click photo to see the full album</p>
                  </div>
            </div>
            </div>
        
            <!-- Left and right controls -->
            <a class="carousel-control-prev" href="#demo" data-slide="prev">
            <span class="carousel-control-prev-icon"></span>
            </a>
            <a class="carousel-control-next" href="#demo" data-slide="next">
            <span class="carousel-control-next-icon"></span>
            </a>
        
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