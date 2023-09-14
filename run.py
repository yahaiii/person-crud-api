from create_app import create_app

app = create_app()

@app.route('/')
def index():
    return "Welcome to My Person API!"

if __name__ == '__main__':
    app.run(debug=True)
