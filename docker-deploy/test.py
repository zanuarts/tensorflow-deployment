import tensorflow as tf

print(tf.__version__)

model = tf.keras.models.load_model('fashion-mnist/1')
print('model loaded')