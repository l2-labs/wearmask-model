<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://l2-labs.com/product/wearmask-neural-network">
    <img src="https://l2-labs.com/storage/app/media/git/logo.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">WEARMASK Model</h3>

  <p align="center">
    WearMask is deep learning model to automatically check whether face is protected with some PPE like mask or not.
    <br />
    Free for none-commercial organizations
    <br />
    <a href="https://www.youtube.com/channel/UCvIxZXAE_N2MsNG7YBJgukw">Demo on YouTube</a>
    <br />
    <a href="https://github.com/l2-labs/wearmask-model/issues">Report Bug</a>
    ·
    <a href="https://github.com/l2-labs/wearmask-model/issues">Request Feature</a>
    ·
    <a href="https://l2-labs.com">Request Commercial License</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Model accuracy](#model-accuracy)
* [Use cases](#use-cases)
* [Android application](#android-application)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Dataset](#dataset)
* [License](#license)
* [Contact](#contact)

## About The Project

New reality requires extended precautions. While others fight about the need of PPE (personal protective equipment) usage to flat the curve we just want to provide automatic solution for those who wants to enforce PPE usage by any reason. Thus we trained Deep Learning Convolution network to classify images to two classes:
- face with not-protected mouth and nose. It includes the cases when mouth or nose are not visible, for example covered by motorcycle helm as we cannot guarantee that it's covered by PPE under helm.
- face with properly applied PPE (i.e. mouth and nose are covered with surgiral or hand-made mask or respirator)

## Model accuracy

Released model accuracy is 94.7% on our testing data. If you need a model with higher accuracy (>99%) please contact us at admin@l2-labs.com. The provided model is available free of charge for non-profit organisations and also on commercial bases for others. We could provide you with the model compatible with various architectures MobileNet, ResNet, etc and frameworks like TF, pytorch and others. We also provide integration services.


## Use cases

Use WearMask model to detect person who do not wear mask in crowd on the street at night:

[![WearMask at night](https://img.youtube.com/vi/9NTc5iziRQU/0.jpg)](https://www.youtube.com/watch?v=9NTc5iziRQU)

Use WearMask model to detect person who do not wear mask in various scenes:

[![WearMask various scenes](https://img.youtube.com/vi/kU26LuM_Azc/0.jpg)](https://www.youtube.com/watch?v=kU26LuM_Azc)

WearMask recognizes correctness of mask/respirators usage:

[![WearMask correctly applied](https://img.youtube.com/vi/6TxmM_1iCvA/0.jpg)](https://www.youtube.com/watch?v=6TxmM_1iCvA)


## Android application

WearMask model is used in WearMask Android app to enforce mask usage for small business. Currently the application is on the google publish review, please send request to admin@l2-labs.com if you want to be in first 100 private testers.

Application scans live video stream from device camera and perform analysis is order to detect person who doesn't wear mask:
![Application screenshot](https://l2-labs.com/storage/app/media/git/26b678d4-b5ad-4f57-bc55-7901bbde0918.jpeg)

If it detects somebody wihtout correctly applied mask/respirators it alarms with audio and visual notifications:
![Application screenshot](https://l2-labs.com/storage/app/media/git/0ef737dd-76c4-4cb5-b820-f28d8d84d3b1.jpeg)

It's specially designed to be used on big screen smartphones or tablets which can be installed in public entrance areas in such a way that the one can see visual notificationson on the screen in case of mandatory face mask violation


## Getting Started
In order to use the model the one needs to clone repository, install dependencies, download and unpack model weights and it's ready to perform image analysis

### Prerequisites
We provide requirements.txt file to automatically setup environment with pip but generally prerequisites are:

1. Python 3.6+
2. Tensorflow 2.2.0+
3. Pillow

### Installation

1. Setup python dependencies:

```
pip install -r requirements.txt
```

2. Download from google storage [pre-trained model](https://drive.google.com/file/d/1ZVCb7Ronzqvrv5Ctc8anVlF0nRDy2flA/view?usp=sharing) and unpack it to the pretrained folder:

```
tar -xzf wearmask-1587835694.tar.gz
```


## Usage
Original [image from flickr](https://www.flickr.com/photos/youngshanahan/49737641203/)

Execute the command to process the image:
```
python test.py images/49737641203_16019ec424_o.jpg
```


## Dataset

Model was trained on data which were available without any legal or ethical restrictions on time of training. Current dataset version is composed of >1M data samples. We are constantly improving coverage of diverse use cases to reduce biases. We couldn't share the dataset in any case as model was trained in online mode without actual dataset collecting and storing. If your business need the similar online training approach feel free to contact admin@l2-labs.com to discuss feasibility of using our tools to train your models.

## License
Source code in the repository is distributed under MIT license
Pre-trained Model weights are distributed under CC BY-NC-ND 4.0


## Contact
If you need model for commercial usage or model as Service or have some special requests feel free to contact via e-mail admin@l2-labs.com