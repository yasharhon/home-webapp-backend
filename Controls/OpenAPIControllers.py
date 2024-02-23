import tornado.web

class RandomDogController(tornado.web.RequestHandler):
    def get(self):
        self.write("This is a random dog")

class RandomOpenAPIController(tornado.web.RequestHandler):
    def get(self):
        self.write("This is a random open web API")
