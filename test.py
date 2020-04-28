from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import argparse
import tensorflow as tf


__author__ = "Alexander Soroka"
__copyright__ = "L2labs, LLC admin@l2-labs.com"
__year__ = "2020"


def main():
    # Parse application arguments
    args = argparse.ArgumentParser()
    args.add_argument(
        '-m', '--model', type=str, default='pretrained',
        help='Pretrained model directory path'
    )
    args.add_argument('image', type=str, help='Image to be processed')
    args = args.parse_args()

    # Load model first
    model = tf.keras.models.load_model(args.model)

    # load image
    image = tf.keras.preprocessing.image.load_img(
        args.image, target_size=[224, 224]
    )

    image = tf.keras.preprocessing.image.img_to_array(image) / 255.

    # Add batch dimension
    image = tf.expand_dims(image, 0)

    # Model output is multidimensional array with first axis for image number in batch,
    # and second for probabilities of two classes: PPE is not presented and PPE is presented
    print('Probability of PPE presence: {}'.format(model(image).numpy()[0, 1]))


if __name__ == "__main__":
    main()