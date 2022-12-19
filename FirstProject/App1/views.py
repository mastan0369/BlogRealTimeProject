from django.shortcuts import render
from django.http import HttpResponse

#Create your views here...
def f11(request): 
    ss='''
    <html>
        <head>
            <title>***welcome page***</title>
            <style>
                h1{
                    color:blue;
                    width:80%;
                  }
                h2{
                    color:red;
                    width:70%;
                   }
                h3{
                    color:pink;
                    width:60%;
                  }
                h4{
                    color:violet;
                    width:50%;
                  }
                h5{
                    color:green;
                    width:40%;
                  }
                h6{
                    color:orange;
                    width:30%;
                  }
                h1,h2,h3{
                    background-color:lightblue;
                    border:2px Solid Brown;
                }
            </style>
        </head>
        <body>
            <center>
                    <h1>hello user </h1>
                    <hr color:yellow width:90%/>
                    <h2>andd</h2>
                    <hr color:yellow width:80%/>
                    <h3>how are you</h3>
                    <hr color:yellow width:70%/>
                    <h4>welcome</h4>
                    <hr color:yellow width:60%/>
                    <h5>glad</h5>
                    <hr color:yellow width:50%/>
                    <h6>nice to meet you</h6>
                    <hr color:yellow width:40%/>
            </center>
        </body>
    </html>
''';
    return HttpResponse(ss);