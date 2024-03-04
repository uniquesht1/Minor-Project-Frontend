from flask import Flask, render_template, request
import matlab.engine

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_picture', methods=['POST'])
def upload_picture():
    if 'picture' in request.files:
        picture = request.files['picture']
        print("Uploaded picture filename:", picture.filename)

        # You can now process the picture as needed
        # For example, save it to a specific folder or perform image processing
        # Here, we'll just return a simple message
        return "Picture accepted! Thank you for the cuteness!"
    else:
        return "No picture uploaded. Please choose a cute picture before submitting."


if __name__ == "__main__":
    app.run(debug=True)
