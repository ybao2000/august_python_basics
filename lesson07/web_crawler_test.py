webpage = """<!DOCTYPE html>
 <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">   
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.1/css/all.css" integrity="sha384-5sAR7xN1Nv6T6+dT2mhtzEpVJvfS3NScPQTrOxhwjIuvcA67KV2R5Jz6kr4abQsz" crossorigin="anonymous">        
        <link rel="stylesheet" type="text/css" href="/static/site.css">
        
<link href = "https://code.jquery.com/ui/1.10.4/themes/ui-lightness/jquery-ui.css" rel = "stylesheet"> 
          
             
            <title>AB Kid Class - Course Attendance</title>
        
    </head>
    <body>
        <header class="site-header">
            <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
                <a class="navbar-brand" href="/">Kid Class</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                    
                        <li class="nav-item">
                            <a class="nav-link" href="/courses">Courses</a>
								</li>
                        <li class="nav-item">
									<a class="nav-link" href="/students">Students</a>
								</li>
								<li class="nav-item">
									<a class="nav-link" href="/timeperiods">Time Periods</a>
								</li>	
                        <li class="nav-item">
                            <a class="nav-link" href="/course_attendance">Attendances</a>
                        </li>
                                                   
                    </ul>
                </div>
                <!-- Navbar Right Side -->
                <div class="navbar-nav">
                    
                        <a class="nav-item nav-link" href="/profile">ybao's Profile</a>                     
                        <a class="nav-item nav-link" href="/logout">Logout</a>                    
                    
                  
                </div>
            </nav>              
        </header>
                 
        <main role="main" class="container">
            <div class="row">
                <div class="col-md-12">
                    
                                               
                    

                    
	 <legend>Course Attendance</legend>
	 <div class="content-section">
		 <form method="POST" action="">
			 <input id="csrf_token" name="csrf_token" type="hidden" value="IjBhYzAyYTE5MzdlOTE0N2IyY2IzYWY5OWYyZjk4MGM0Y2MzMmE5MGUi.X0hTHQ.qzlYomzBl52StOWD_XmBSzKidQU">
			 <fieldset class="form-group">
				 <div class="row">
					<div class="col-md-4">
						<label class="form-control-label" for="course">Course</label>
						
							 <select class="form-control form-control-lg" id="course" name="course"><option value="6">Basic Programming</option><option value="4">Python Basics</option><option value="5">Python Web Development</option><option selected value="11">August Camp: Python Basics</option><option value="10">Summer Camp: Web Development</option><option value="9">Summer Camp: Python Basics</option></select>                                     
											 
					 </div>
					 <div class="col-md-4">
						<label class="form-control-label" for="date">date</label>
						<input class="form-control form-control-lg" id="date" name="date" type="date" value="2020-08-27">
					</div>
					<div class="col-md-4">
						<label class="form-control-label" for="timeperiod">Timeperiod</label>
						
							 <select class="form-control form-control-lg" id="timeperiod" name="timeperiod"><option value="2">1:00pm - 2:30pm</option><option value="3">3:00pm - 4:30pm</option><option selected value="5">6:30pm - 8:30pm</option><option value="4">6:30pm - 8:00pm</option><option value="1">10:00am - 11:30am</option><option value="6">10:00am - 12:00pm</option></select>                                     
											 
					 </div>					
				 </div>				 
			 </fieldset>
			 <div class="form-group">
				<input class="btn btn-outline-info" id="submit" name="submit" type="submit" value="Refresh">
		  	</div>
		 </form>
	 </div>
	 
	 	<div class="container" id="ts">
			<a
				href="/export_excel?course_id=11&amp;date=2020-08-27&amp;timeperiod_id=5"
				class="btn btn-primary btn-sm mt-1 mb-1"
			>
				<i class="fa fa-file-excel-o"></i> export to excel
			</a>
			<a
			href="/export_pdf?course_id=11&amp;date=2020-08-27&amp;timeperiod_id=5"
			class="btn btn-primary btn-sm mt-1 mb-1"
			>
				<i class="fa fa-file-pdf-o"></i> export to pdf
			</a>
			 <div class="row ts-start">
				<div class="col-md-2">Student</div>
				<div class="col-md-1">Attend?</div>
				<div class="col-md-3">Last Description</div>
				<div class="col-md-6">Description</div>
			 </div>
			 
			  	<div class="row">
					<div class="col-md-2">Alex Han</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=52&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								 Yes 
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6">  </div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">Andrew Li</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=53&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6"></div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">Bill Zhou</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=58&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								 Yes 
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6">  </div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">Brandon Cheng</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=19&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								 Yes 
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6">  </div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">David Ma</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=55&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								 Yes 
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6">  </div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">David Qiao</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=44&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								 Yes 
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6">  </div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">Emmett Chen</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=50&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6"></div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">Mira Zheng</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=29&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6"></div>
				</div>
			 
			  	<div class="row">
					<div class="col-md-2">Selina Yang</div>
					<div class="col-md-1 no-padding">
						<a href="/edit_attendance?course_id=11&amp;student_id=56&amp;date=2020-08-27&amp;timeperiod_id=5">
							<button type="button" class="btn btn-link full-size">
								
							</button>
						</a>
					</div>
					<div class="col-md-3"></div>					
					<div class="col-md-6"></div>
				</div>
			 
		 </div>
		 
		 <br>
		 <div>
			 Total: 5/9
		</div>
		
	 

                </div>
            </div>
        </main>

        <script
        src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
        crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>    
        
    <script src = "https://code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
    <script type="text/javascript">
        $( document ).ready(function() {
					$("#courseoption").on('selectmenuchange', function() {
						alert('fucsdsdk');
					})	     
        });    
    </script>
        
    </body>
</html>"""

def get_name(string):
    	#				<div class="col-md-2">Alex Han</div>
  index1 = string.index(">")
  index2 = string.index("</div>")
  return string[index1+1:index2]

# get all the names from the web page
lines = webpage.split("\n")
# print(len(lines))

count = 0
result = []
# for line in lines:
while count < len(lines): # using while loop and index instead of for loop
  line = lines[count]
  text = line.strip()
  if text == """<div class="row">""":
    print("we got the location")
    count += 1
    line = lines[count].strip()
    if line.startswith("""<div class="col-md-2">"""):
  	#				<div class="col-md-2">Alex Han</div>        
      print("This is the line")
      name = get_name(line)
      result.append(name)
  count += 1

print(result)
