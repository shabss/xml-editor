#!python
import os.path
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy


class Root:
    @cherrypy.expose
    def index(self):
        return """<html>
<head>
        <title>CherryPy static example</title>
</head>
<body>
<!--<a href="./static/demo/basic/index.html">Demo</a> -->
<a href="./static/editor.html">Editor</a>
<p>Static example</p>
</body>
</html>"""

xmlconf = os.path.join(os.path.dirname(__file__), 'xmlEditor.conf')

if __name__ == '__main__':
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(Root(), config=xmlconf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(Root(), config=xmlconf)