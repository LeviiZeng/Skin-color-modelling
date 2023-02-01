#Implement a Gaussian mixture model to fit the distribution of the skin colors

(1) Given skin and background pixels, you are required to convert the RGB color values into YCbCr space, then draw the distribution of skin colors using Cb and Cr values in a two-dimensional space. Note that thesamples from skin and background shall be marked using different types of dots and colors.

(2) Build a Gaussian mixture model to fit the distribution of skin colors (Cb and Cr), use the available skin samples to estimate the mean 𝜇 and covariance matrix Σ of such a distribution. Pls see appendix for details about Gaussian mixture model

(3) Given the test image, input the Cb and Cr of each pixel to the Gaussian mixture model to predict the probability of each pixel belonging to skin, and visualize the probability map with a gray level image (same size with the input).

![1675236130553](https://user-images.githubusercontent.com/92025034/215977546-564894a4-fc5c-41a1-983d-5fb74d361d0d.png)
