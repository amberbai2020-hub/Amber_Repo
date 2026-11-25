#Help files import from the directory
#Acts as the entry point into a given directory. When we tell Flask to run an app developed
#in the directory, it will look for this file and run it first

from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes
from web_app.routes.stocks_routes import stocks_routes
#from web_app.routes.book_routes import book_routes
#from web_app.routes.weather_routes import weather_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    app.register_blueprint(stocks_routes)
    #app.register_blueprint(book_routes)
    #app.register_blueprint(weather_routes)
    return app

#Import commandline logic from the commandline file into the web application interface
#Route: Tells the web application what to do when someone visits a certain URL in the browser, denoted by the route decorators

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)