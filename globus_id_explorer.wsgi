import sys

sys.path.insert(0, '/soft/globus-id-explorer/globus-id-explorer')
from globus_id_explorer import app as application

if __name__ == '__main__':
    application.run()
