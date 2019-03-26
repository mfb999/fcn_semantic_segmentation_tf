from network import Network

class VGG_ILSVRC_16_layers(Network):
    def setup(self):
        (self.feed('data')
             .conv(3, 3, 64, 1, 1,  name='VGG/conv1_1', trainable=True)
             .conv(3, 3, 64, 1, 1,  name='VGG/conv1_2', trainable=True)
             .max_pool(2, 2, 2, 2,  name='VGG/pool1')
             .conv(3, 3, 128, 1, 1, name='VGG/conv2_1', trainable=True)
             .conv(3, 3, 128, 1, 1, name='VGG/conv2_2', trainable=True)
             .max_pool(2, 2, 2, 2,  name='VGG/pool2')
             .conv(3, 3, 256, 1, 1, name='VGG/conv3_1', trainable=True)
             .conv(3, 3, 256, 1, 1, name='VGG/conv3_2', trainable=True)
             .conv(3, 3, 256, 1, 1, name='VGG/conv3_3', trainable=True)
             .max_pool(2, 2, 2, 2,  name='VGG/pool3')
             .conv(3, 3, 512, 1, 1, name='VGG/conv4_1', trainable=True)
             .conv(3, 3, 512, 1, 1, name='VGG/conv4_2', trainable=True)
             .conv(3, 3, 512, 1, 1, name='VGG/conv4_3', trainable=True)
             .max_pool(2, 2, 2, 2,  name='VGG/pool4')
             .conv(3, 3, 512, 1, 1, name='VGG/conv5_1', trainable=True)
             .conv(3, 3, 512, 1, 1, name='VGG/conv5_2', trainable=True)
             .conv(3, 3, 512, 1, 1, name='VGG/conv5_3', trainable=True)
             .max_pool(2, 2, 2, 2,  name='VGG/pool5')
             .conv(7, 7, 4096, 1, 1, name='VGG/fc6', biased=True)
             .dropout(name='VGG/drop6')
             .conv(1, 1, 4096, 1, 1, name='VGG/fc7', biased=True)
             .dropout(name='VGG/drop7'))
