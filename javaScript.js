//Global Variables
var color = "black";
var clicks = new Array();
var shape=1;
var i=0;
var ctx;

window.onload = function() {
	var canEl = document.getElementById("myCanvas");
	if(canEl && canEl.getContext) {
			var contextObj = canEl.getContext("2d");
			if (contextObj) {
				ctx=contextObj;
				canEl.addEventListener('click', function(evt) {
	 			  	var mousePos = getMousePos(canEl, evt);
	   				clicks[i] = mousePos;
	      
				   	i++;
				   	if (i==2 && shape!=4)
				   	{
				  		switch(shape)
				   		{
				   			case 1:
				   				console.log("drawing line");
				   				drawLine(clicks[0].x,clicks[0].y,clicks[1].x,clicks[1].y);
				   				break;
				   			case 2:
				   				console.log("drawing circle");
				   				drawCircle(clicks[0].x,clicks[0].y,clicks[1].x,clicks[1].y);
				   				break;
				   			case 3:
				   				console.log("drawing polygon");
				   				drawPoly(clicks[0].x,clicks[0].y,clicks[1].x,clicks[1].y);
				   				break;
				   		}
				   	}
					else{
						if (i==4&&shape==4){
							console.log("drawing curve")
							drawCurve(clicks[0].x,clicks[0].y,clicks[1].x,clicks[1].y,clicks[2].x,clicks[2].y,clicks[3].x,clicks[3].y);
						}
					}
				}, false);
			}
    	}
 }
 
 
//Change drawing color
function setColor(selected){  
	color = selected;	
}

function setShape(shapeNum){
	shape=shapeNum;
}

//Get mouse click
function getMousePos(canvas, evt){
   var rect = canvas.getBoundingClientRect();
   return {
     x: evt.clientX - rect.left,
     y: evt.clientY - rect.top
    };
}

function drawLine(x0,y0,x1,y1){
	var dx = Math.abs(x1-x0);
	var dy = Math.abs(y1-y0);
	var sx = (x0 < x1) ? 1 : -1;
	var sy = (y0 < y1) ? 1 : -1;
	var err = dx-dy;
	
	while(true){
		drawPixel(x0,y0);  // Do what you need to for this
		if ((x0==x1) && (y0==y1)) break;
		var e2 = 2*err;
		if (e2 >-dy){ err -= dy; x0  += sx; }
		if (e2 < dx){ err += dx; y0  += sy; }
	}  
	i=0;
	return true;
}

function drawCircle(x0, y0, x1, y1)
{
	var xDiff = Math.pow((x0 - x1),2);
	var yDiff = Math.pow((y0 - y1),2);
	var radius = Math.sqrt(xDiff + yDiff);
	var x = radius, y = 0;
  	var radiusError = 1-x;

	while(x >= y)
	{
	  drawPixel(x + x0, y + y0);
	  drawPixel(y + x0, x + y0);
	  drawPixel(-x + x0, y + y0);
	  drawPixel(-y + x0, x + y0);
  	  drawPixel(-x + x0, -y + y0);
	  drawPixel(-y + x0, -x + y0);
	  drawPixel(x + x0, -y + y0);
	  drawPixel(y + x0, -x + y0);
	  y++;
	  if (radiusError<0)
	  {
	  	radiusError += 2 * y + 1;
	  } else {
		    x--;
		    radiusError+= 2 * (y - x + 1);
		   }
	  }
	  i=0;
}

function drawCurve(x0, y0, x1, y1, x2, y2, x3, y3){
console.log("in function");
			console.log(x0+" "+y0+" "+x1+" "+y1+" "+x2+" "+y2+" "+x3+" "+y3)
			var currX, currY, prevX = x0, prevY = y0;
			var aX, bX, cX, dX;
			var aY, bY, cY, dY;
			var t, linesNum, stepSize;
		
			// Matrix - X
			dX = x0;
			cX = (3*x1) - (3*x0);
			bX = (3*x2) - (6*x1) + (3*x0);
			aX = x3 - (3*x2) + (3*x1) - x0;
		
			// Matrix Y
			dY = y0;
			cY = (3*y1) - (3*y0);
			bY = (3*y2) - (6*y1) + (3*y0);
			aY = y3 - (3*y2) + (3*y1) - y0;
		
			linesNum = document.getElementById("curve_lines").value;
			stepSize = 1/linesNum;
			console.log(linesNum+" "+stepSize);
		ctx.beginPath();
			for (t = 0; t <= 1; t += stepSize){
				console.log("done here "+t);
				currX = aX*Math.pow(t, 3) + bX*Math.pow(t, 2) + cX*t + dX;
				currY = aY*Math.pow(t, 3) + bY*Math.pow(t, 2) + cY*t + dY;
				console.log(currX+" "+currY);
				ctx.moveTo(prevX,prevY);
				ctx.lineTo(currX,currY);
				prevX = currX;
				prevY = currY;
			}
			
			ctx.strokeStyle = color;
			ctx.lineWidth = 1;
			ctx.stroke();
			i=0;
			repaint();
		}

function drawPoly(x0,y0,x1,y1){
	var numberOfSides = document.getElementById('sides').value;
    var Xcenter = x0, Ycenter = y0;
    
    var xDiff = Math.pow((x0 - x1),2);
	var yDiff = Math.pow((y0 - y1),2);
	var radius = Math.sqrt(xDiff + yDiff);
 
	ctx.beginPath();
	ctx.moveTo (Xcenter +  radius * Math.cos(0), Ycenter +  radius *  Math.sin(0));          
 
	for (var t = 1; t <= numberOfSides;t += 1) {
    ctx.lineTo (Xcenter + radius * Math.cos(t * 2 * Math.PI / numberOfSides), Ycenter + radius * Math.sin(t * 2 * Math.PI / numberOfSides));
	}
 
	ctx.strokeStyle = color;
	ctx.lineWidth = 1;
	ctx.stroke();
	i=0;
	return true;
}

function drawPixel(x,y,c){
	ctx.fillStyle = color;
	ctx.fillRect(x,y,1.5,1.5);
}  	