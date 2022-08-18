from flask import Flask, Response, request
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    CORS(app)
    


    @app.before_request
    def basic_authentication():
        if request.method.lower() == 'options':
            return Response()



    app.config['SECRET_KEY'] = 'hdgaiudhgasdipova'
    

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app