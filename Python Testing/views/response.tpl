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

<body onload="showincolor()">
  <!--<button type="button" id="btnSave" onclick="save()" class="button" style="display:block;
  margin:0 auto;">Download Copy of Switch Ports</button> -->

  <h1 id="title" style="text-align: center;">Switch {{hostname}}</h1>
  <h3 style="text-align: center;">{{uptime}}</h3>
<table id='txtdata' class="table table-striped">
  <tr>
    <th>Interface</th>
    <th>Utilized</th>
    <th>VLAN</th>
    
    
    
  </tr>
  %for inter, interinfo in data.items():
    <tr >
      
      <td>{{inter}}</td>
      %for key in interinfo:
      <td id='datarow' >
        {{interinfo[key]}} 
      </td>
     
      
      %end
      
     </tr>
      
  </tr>
  %end
</table>
<hr/>

<hr/>
<script>

function save() {
      var data = document.getElementById("txtdata").innerHTML;
      var c = document.createElement("a");
      var asaname = '{{hostname}}';
      /*
      var d = new Date(date),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate(),
      year = d.getFullYear();

      if (month.length < 2) 
          month = '0' + month;
      if (day.length < 2) 
          day = '0' + day;

      var currentdate = year+month+day
      */
      
      c.download = "Copy of Ports Used for "+asaname+".txt";

      
      
      var t = new Blob([data], {
      type: "text/plain"
      });
      c.href = window.URL.createObjectURL(t);
      c.click();
    }

/*
function showincolor() {
  var table = document.getElementById('mytable');   

  var rows = mytable.getElementsByTagName("tr"); 

  for(i = 0; i < rows.length; i++){           

//manipulate rows 

    if(i % 2 == 0){ 

      rows[i].className = "even"; 

    }else{ 

      rows[i].className = "odd"; 

    }       


}}
*/
  /*
function showincolor(){
  var datarow2 = document.getElementById("datarow").innerHTML;
  console.log('Right before printing of data row')
  console.log(datarow2)
  if (datarow2.includes("Yes")){
    console.log('Inside of Yes if statment')
    
    document.getElementById("datarow").style.backgroundColor = 'red';

  }
  if (datarow2.includes('No')){
    document.getElementById("datarow").style.backgroundColor = 'green';
    

  }}*/
</script>
</body>
</html>