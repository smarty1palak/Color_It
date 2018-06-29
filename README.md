# Color_It
A repository which will contain works related to recolouring the image using deep learning.

## Research Papers I am planning to follow:

<https://richzhang.github.io/colorization/resources/colorful_eccv2016.pdf>

#### Summary:
Given the lightness channel L, our system predicts the corresponding a and b color channels of the image in the CIE Lab colorspace.<br/>
Color prediction is inherently multimodal – many objects can take on several plausible colorizations. For example, an apple is typically red, green, or yellow, but unlikely to be blue or orange. To appropriately model the multimodal nature of the problem, we predict a distribution of possible colors for each pixel.<br/>
Re-weight the loss at training time to emphasize rare colors.. Lastly, we produce a final colorization by taking the annealedmean of the distribution<br/>
Tasks: <br/>
(a) designing an appropriate objective function that handles the multimodal uncertainty of the colorization problem and captures a wide diversity of colors, <br/>
(b) introducing a novel framework for testing colorization algorithms, potentially applicable to other image synthesis tasks, and <br/>
(c) setting a new high-water mark on the task by training on a million color photos.<br/>

We use a classification loss, with rebalanced rare classes. We use a single-stream, VGG-styled network with added depth and dilated convolutions<br/>
Trained on ImageNet<br/>

Arthitecture: <br/>
Each conv layer refers to a block of 2 or 3 repeated conv and ReLU layers, followed by a BatchNorm layer. The net has no pool layers. All changes in resolution are achieved through spatial downsampling or upsampling between conv blocks.
