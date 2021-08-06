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
      <h1 style="padding-top: 100px;">John's Higher View's Login Reset</h1>

    <form action="/reset/{{username}}/{{reset_token}}" method="post" class="form" style="text-align: center; padding-top: 100px;">
        <label><b>Username: {{username}} </b></label><br/>
        
        <label><b>Password</b></label><br/>
        <input type="password" name="password"/><br/>
        <label><b>Password Again:</b></label><br/>
        <input type="password" name="password_again"/><br/>
        <br>
        <input type="hidden" name="csrf_token" value="{{csrf_token}}"/>
        <input type="submit" value="Reset Password" class="btn btn-primary"/>

    </form>

    <div style="padding-top: 25px">
       <a href="/forgot"> <input type="button" value="Forgot Password?" class="btn btn-secondary" /> </a>
    </div>

</div>
</html>