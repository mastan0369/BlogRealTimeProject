from django.shortcuts import render;
from django.http import HttpResponse;

#Create your views here...
def f1(request): 
    ss='''
    <html>
        <head>
            <title>FROM MASTAN VALI SHAIK</title>
            <style>
                h1{
                    color:red;
                    width:50%;
                }
                h2{
                    color:red;
                }
                h3{
                    color:red;
                }
                h4{
                    color:red;
                }
                h5{
                    color:red;
                }
                h6{
                    color:red;
                }
                
            </style>
        </head>
	
        <body>
            <center>
                <h6>I LOVE YOU </h6>
                
                <h5>hi</h5>
                
                <h4>hi</h4>
                
                <h3>hi</h3>
              
                <h2>hi</h2>
               
                <h1>hi</h1>
                
            </center>
        </body>
    </html>'''

    return HttpResponse(ss);