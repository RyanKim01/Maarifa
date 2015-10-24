from flask import Flask

app = Flask(__name__)

top_of_page = """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1"/>


<style>
    body{
        margin:0;
        font-family:Arial, Helvetica, sans-serif;
    }
    #topbar{
        height:50px;
        width: auto;
        background-color: #222222;
        color: #999999;
        text-align: center;
    }
    #topbar p{
        padding: 15px;
    }
    #logodiv{
        float:left;
        height: 50px;
        width: 50px;
        border-right: 1px grey solid;
    }
    #navbar{
        height:50px;
        width: auto;
        color: #999999;
    }
    #navbar table{
        text-align: center;
    }
    #navbar td{
        padding: 15px;
        border-left: 1px grey solid;
        background-color: #999999;
    }
    a:active  {background-color:#4aa3df; text-decoration:underline}
</style>

<title>Maarifa - Knowledge</title>
</head>

<body>

    <div id="container">
        <div id="topbar">
            <div id="logodiv">
                <a href="./"><img src="images/BBC Logo.png"/></a>
       		</div>
            <p>World-class Knowledge, Everywhere</p>
        </div>

        <div id="navbar">
            <table style="width: 100%">
                <tr>
                    <td><a href="./Eng">English</a></td>
                    <td><a href="./Math">Math</a></td>
                    <td><a href="./Sci">Science</a></td>
                </tr>
            </table>
        </div>
    </div>

    <div id="content">"""

bottom_of_page = """    </div>

</body>
</html>"""

@app.route('/')
def index():
    page = top_of_page + "Home Page stuff" + bottom_of_page

    return page

@app.route('/Math')
def math():
    page = top_of_page + "Math Page stuff" + bottom_of_page

    return page

@app.route('/Eng')
def eng():
    page = top_of_page + "English Page stuff" + bottom_of_page

    return page

@app.route('/Sci')
def sci():
    page = top_of_page + "Science Page stuff" + bottom_of_page

    return page

if __name__ == '__main__':
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
