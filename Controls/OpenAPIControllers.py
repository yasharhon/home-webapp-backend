import jsonpickle
import tornado.web
import webappclasses.randomDogWrapper as randomDog
import webappclasses.randomPublicAPIWrapper as randomPublicAPI

class RandomDogController(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
    
    def get(self):
        wrapper = randomDog.randomDogWrapper.makeFromConfig("Configs/randomDogConfig.json")
        
        res = wrapper.getData()
        
        self.write(jsonpickle.encode(res, unpicklable=False))

class RandomOpenAPIController(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
    
    def get(self):
        wrapper = randomPublicAPI.randomPublicAPIWrapper.makeFromConfig("Configs/randomPublicAPIConfig.json")

        res = wrapper.getData()
        
        self.write(jsonpickle.encode(res, unpicklable=False))
