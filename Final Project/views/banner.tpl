


<div class="row" id="nav">
  <div class="col-sm" style="text-align: center; margin:auto">
    <a href="/">  <b>Home</b> </a>
  </div>
  
  <div class="col-sm" style="text-align: center; margin:auto">
     <a href="/parklocations"><b> Park Geographic Locations</b></a>
  </div>
  
  

 %if user:
 <div class="col-sm"style="text-align: center; margin:auto">
  <b>Welcome, {{user}}! &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp</b><a href="/logout"><b> Logout</b></a>
</div>
%else:
<div class="col-sm"style="text-align: center; margin:auto">
  <a href="/login"><b>Login</b></a>
</div>
%end
</div>
 
 
