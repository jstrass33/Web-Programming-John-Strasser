<html>
    %include header
    
<body>
    <form action="/comments" method="post" style="text-align: center;">
        <input type="hidden" name="nationalpark" value='yosemite' display='None' />
        Username <input type="text" name="username"/><br> <br>
        Add Comment <br>
        <textarea type="text" name="comment" class='media-body' style="width:800px; margin:0 auto; border-style: groove; margin-bottom: 10px; height: 100px;">Enter a new comment...</textarea><br>
        <hr/>
        <input type="submit" class="btn btn-primary"value="Submit"/>
        </form>

<p style="text-align: center;"><b>{{commentsnumber}} New Comments </b></p>
<hr>

%for item in items:
<div class='media-body' style="width:800px; margin:0 auto; border-style: groove; margin-bottom: 10px;">

        <img src="/static/avatar.png" alt="Avatar" class="float-left"  style="width: 30px; height:30px; padding-left: 5px; padding-top: 5px;"/> 
        <p style="margin-left: 40px; margin-top: 5px;"><b>{{item['username']}}</b> made a comment</p>
        
      
      
        
       <p style="padding-left: 75px;">
        {{item['comment']}}
        %if 'jstrasse' in item['username']:
        <a href="/delete/{{nationalpark}}/{{item['id']}}" style="float: right; margin-right: 10px;"><span class="material-icons">
            delete
            </span></a>
        </p>
    
       
       %end

</div>



%end


<hr/>
</body>
</html>