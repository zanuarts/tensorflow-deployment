import tensorflow as tf

# Convert Model
converter = tf.lite.TFLiteConverter.from_saved_model('fashion-mnist/1')
tflite_model = converter.convert()

# Save model
with open('model.tflite', 'wb') as f:
    f.write(tflite_model)