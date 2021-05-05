import cherrypy

class Formulario(object):
    @cherrypy.expose
    def form(self):
        cherrypy.response.headers["Content-Type"] = "text/html"
        return open("formulario.html")

class Actions(object):
    @cherrypy.expose
    def doLogin(self , username = None , password = None):
        return "Verificar as credenciais do utilizador " + username
    

cherrypy.quickstart(Formulario())
