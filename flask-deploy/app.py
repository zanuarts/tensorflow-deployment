from flask import Flask
from flask import request
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('fashion-mnist/1')

@app.route('/predict', methods=['POST'])
def predicts():
    print(request.headers)
    instances = request.json["data"]
    print(instances)
    result = model.predict(instances)
    return {"predictions" : result.tolist()}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')