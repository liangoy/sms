import connexion
import logging

from gevent import monkey
monkey.patch_all()

logging.basicConfig(level=logging.INFO)
app = connexion.App('main')
app.add_api('apis/swagger.yaml')
application = app.app
if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=6678, server='gevent')