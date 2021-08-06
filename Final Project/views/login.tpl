<html>
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
</style>



<div id="main" class="jumbotron main"> 
    
    <div id="transparent">
        %if error != '':
            %include alert
        %end
      <h1 style="padding-top: 100px;">John's Higher View's Login</h1>

    

    <form action="/login" method="post" class="form" style="text-align: center; padding-top: 100px;">
        <label><b>Username </b></label><br/>
        <input type="text" name="username"/><br/>
        <label><b>Password</b></label><br/>
        <input type="password" name="password"/><br/>
        <br>
        <button type="submit" id="submit"value="Login" class="btn btn-primary" onclick="loading()"><strong>Login</strong></button>

    </form>

    <div style="padding-top: 25px">
       <a href="/forgot"> <input type="button" value="Forgot Password?" class="btn btn-secondary" /> </a> <br> <br>
       <a href="/signup"> <input type="button" value="Click to Sign-Up" class="btn btn-secondary"/> </a>
    </div>

</div>
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