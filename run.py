from app import create_app

ja_app = create_app()

if __name__ == '__main__':
    ja_app.run(host='0.0.0.0', debug=True)