import web

urls = (
        '/thermostat/(\w+)', 'thermostat',
        '/thermostat/(\w+)/name', 'name',
        '/thermostat/(\w+)/temp', 'name',
        )

class thermostat:
    def GET(self, name):
        return name

class name:
    def GET(self, id):
        return 'you get'

    def PUT(self, id):
        name = web.data()
        return 'you put'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
