import asyncio
import tornado
import tornado.web
import Controls.OpenAPIControllers

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/controls/openapis/randomdog", Controls.OpenAPIControllers.RandomDogController),
        (r"/controls/openapis/randomopenapi", Controls.OpenAPIControllers.RandomOpenAPIController),
    ])

async def main(portNo):
    app = make_app()
    app.listen(portNo)
    await asyncio.Event().wait()

if __name__ == "__main__":
    portNo = 8888

    print("Starting webserver, get hello world at http://localhost:" + str(portNo) + ".")
    
    asyncio.run(main(portNo))
