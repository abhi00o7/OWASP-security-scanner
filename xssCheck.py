import os
 
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
 
page_header = """
<!doctype html>
<html>
  <head>
    <link rel="stylesheet" href="/static/styles.css" />
  </head>
 
  <body id="reflected-demo">
    <img src="/static/demos/bobazillion.png">
      <div>
"""
 
page_footer = """
      <script>top.postMessage(window.location.toString(), "*");</script>
    </div>
  </body>
</html>
"""
 
main_page_markup = """
<form action="" method="GET">
  <input id="query" name="query" value="Enter query here..."
    onfocus="this.value=''">
  <input id="button" type="submit" value="Search">
</form>
"""
 
class MainPage(webapp.RequestHandler):
 
  def render_string(self, s):
    self.response.out.write(s)
 
  def get(self):
    # Disable the reflected XSS filter for demonstration purposes
    self.response.headers.add_header("X-XSS-Protection", "0")
 
    if not self.request.get('query'):
      # Show main search page
      self.render_string(page_header + main_page_markup + page_footer)
    else:
      query = self.request.get('query', '[empty]')
       
      # Our search engine broke, we found no results :-(
      message = "Sorry, no results were found for <b>" + query + "</b>."
      message += " <a href='?'>Try again</a>."
 
      # Display the results page
      self.render_string(page_header + message + page_footer)
     
    return
 
application = webapp.WSGIApplication([ ('.*', MainPage), ], debug=False)
 
def main():
  run_wsgi_app(application)
 
if __name__ == '__main__':
  main()