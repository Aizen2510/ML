import tensorflow as tf


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if (logs.get('accuracy') > 0.85):
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True

callbacks = myCallback()
data = tf.keras.datasets.fashion_mnist #dataset tu keras

(training_images, training_labels), (test_images, test_labels) = data.load_data() # tra ve tap du lieu huan luyen

# chuan hoa hinh anh
training_images = training_images / 255.0
test_images = test_images / 255.0

# xay dung mang no ron
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),# ham kich hoat relu
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)# ham kich hoat softmax
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=50, callbacks=[callbacks])
model.evaluate(test_images, test_labels)
classifications = model.predict(test_images)
print(classifications[5]) # so luong phan tu trong mang kq
print(test_labels[5])
