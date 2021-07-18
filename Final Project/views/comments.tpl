<html>
    %include header
<body>


%for item in items:
<div>
        {{item['username']}}
      
        %if 'jstrasse' in item['username']:
        <a href="/delete/{{nationalpark}}/{{item['id']}}"><span class="material-icons">
            delete
            </span></a>
       %end
        
        
</div>     

 <div>
        {{item['comment']}}

</div>


%end

<form action="/comments" method="post">
Username <input type="text" name="username"/><br>
Add Comment <input type="text" name="comment"/><br>
<hr/>
<input type="submit" value="Submit"/>
</form>
<hr/>
</body>
</html>