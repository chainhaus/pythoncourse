'''
Assignment #5

1. Add / modify code ONLY between the marked areas (i.e. "Place code below")
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 05_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch

http://flask.pocoo.org/docs/1.0/quickstart/

Using the flask web server, load the HTML form contained in the variable main_page. The form should load at route '/'.
The user should then be able to enter a number and click Calculate at which time the browser will submit
an HTTP POST to the web server. The web server will then capture the post, extract the number entered
and display the number multiplied by 5 on the browser.

Hint: The HTML in main_page needs a modification in the text input. The modification should be done using regular expressions (regex)


'''

from flask import Flask, request
import re

main_page = '''
<html>
    <head>
    <title></title>
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.min.css">
    </head>
<body>
<form class="form-horizontal" method="post" action="/calc">
<fieldset>

<!-- Form Name -->
<legend>Multiplier</legend>

<!-- Text input-->
<div class="form-group">
  <label class="col-md-4 control-label" for="textinput">Number</label>  
  <div class="col-md-4">
  <input id="textinput" type="number" placeholder="Enter a number" class="form-control input-md">
  </div>
</div>

<!-- Button -->
<div class="form-group">
  <label class="col-md-4 control-label" for="singlebutton"></label>
  <div class="col-md-4">
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Calculate</button>
  </div>
</div>

</fieldset>
</form>
<script src="http://netdna.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>
</body>
</html>
'''
    # ------ Place code below here \/ \/ \/ ------







    # ------ Place code above here /\ /\ /\ ------
