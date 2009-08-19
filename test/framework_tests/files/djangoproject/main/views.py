# Create your views here.
from django.http import HttpResponse

def root(request):
    return HttpResponse(page)


page = """    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
       "http://www.w3.org/TR/html4/strict.dtd">

    <html lang="en">
    <head>
    	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    	<title>windmill_js_unit</title>
    	<meta name="generator" content="TextMate http://macromates.com/">
    	<meta name="author" content="Adam Christian">
    	<!-- Date: 2007-09-04 -->
    	<script type="text/javascript" charset="utf-8">
    		//A namespacing test for the jsid fix
    		var testSpace = new function () {
    			this.spaceId = 'jsidTeset';
    		}
    		var countdown = function(){
    			slept = function(){
    				document.getElementById('sleeper').innerHTML = 'Slept';
    			}
    			setTimeout('slept()',10000);
    		}

    		var makeNode = function(){
    			docreate = function(){
    				var n = document.createElement('div');
    				n.id = 'created';
    				n.style.width = '200px';
    				n.style.height = '50px';
    				n.style.border = '2px solid brown';
    				n.innerHTML = 'Hi im the new created node you are waiting for';
    				document.getElementById('amIhere').appendChild(n);
    			}
    			setTimeout('docreate()', 15000);
    		}

    	</script>
    </head>
    <body>
    <form id="frmfrm" action="#" onSubmit="return false;">
    	<input type="text" name="junkfield" value="" id="junkfield"><BR>
    	<INPUT id="cougar" type="radio" name="animal" value="cougar"> Cougar<BR>
      <INPUT id="duck" type="radio" name="animal" value="duck"> Duck<BR><BR>
    	<INPUT name="history_illness" id="Smallpox"
             type="checkbox" 
             value="Smallpox" tabindex="20"> Smallpox
      <INPUT name="history_illness" id="Mumps"
             type="checkbox" 
             value="Mumps" tabindex="21"> Mumps
      <INPUT name="history_illness" id="Dizziness"
             type="checkbox" 
             value="Dizziness" tabindex="22"> Dizziness<BR><BR>

    	<textarea id="story" name="story" rows="8" cols="40"></textarea><br>
    	<SELECT NAME="flavor" id="flavor">
        <OPTION VALUE=a SELECTED>Vanilla
        <OPTION VALUE=b>Strawberry
        <OPTION VALUE=c>Rum and Raisin
        <OPTION VALUE=d>Peach and Orange
       </SELECT>
    	<p><input type="submit" value="Submit">
    </form>
    	<p><input id="subBtn" type="button" value="Start Count" onclick="countdown()">
    	<p><input id="wfeBtn" type="button" value="Test waits.forElement" onclick="makeNode()">

    <div id="sleeper" style="width:200px;height:50px;border:1px solid pink;"></div><br>

    <div id="clickme" style="width:200px;height:50px;border:1px solid blue;" onclick="document.getElementById('clickme').innerHTML = 'Clicked';"></div><br>

    <div id="dblclickme" style="position:relative;width:200px;height:50px;border:1px solid green;" ondblclick="document.getElementById('dblclickme').innerHTML = 'Double Clicked';"></div><br>

    <div id="mousedownme" style="position:relative;width:200px;height:50px;border:1px solid red;" onmousedown="document.getElementById('mousedownme').innerHTML = 'mouse downed';"></div><br>

    <div id="mouseupme" style="position:relative;width:200px;height:50px;border:1px solid purple;" onmouseup="document.getElementById('mouseupme').innerHTML = 'mouse upped';"></div><br><br>

    <div id="mouseoverme" style="position:relative;width:200px;height:50px;border:1px solid purple;" onmouseover="document.getElementById('mouseoverme').innerHTML ='mouse overred';" onmouseout="document.getElementById('mouseoverme').innerHTML = 'mouseouted';"></div><br>


    <div id="amIhere" style="width:200px;height:50px;border:1px solid black;"></div><br>

    <div id="jsidTeset" style="width:200px;height:50px;border:1px solid orange;"></div>
    </body>
    </html>
"""