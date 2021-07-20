<html>
<head>
    %include header
    <style>
        #main{
            height: 1200px;

            text-align: center;
            background-image: url("/static/banff.jpg");
            background-size: 100% 100%;
        

        }
        #transparent{
            background-color: rgba(255,255,255,0.6);
            height: 300px;
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
        

    </style>
</head>
<body>
   





<div class="row" id="nav">
    <div class="col-sm" style="text-align: center; margin:auto">
      <a href="www.google.com">  <b>Photo Gallery</b> </a>
    </div>
    <div class="col-sm" style="text-align: center; margin:auto">
       <a href="www.google.com"><b> Hiking Tips Per Park</b></a>
    </div>
    <div class="col-sm"style="text-align: center; margin:auto">
       <a href="www.google.com"><b>John's Top Hikes</b></a>
    </div>
  </div>

  <div id="main" class="jumbotron"> 
      <div id="transparent">
      <h1 style="padding-top: 100px;">Higher View's</h1>
     <h3 style="padding-top: 25px;">John's Advice for North American Hiking</h3>
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