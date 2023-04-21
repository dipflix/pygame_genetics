import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img = Image.open('image.jpg')

# Convert the image to RGB
img = img.convert('RGB')

# Convert the image to a NumPy array
rgb_array = np.array(img)

# Split the RGB array into R, G, and B channels
R = rgb_array[:, :, 0]
G = rgb_array[:, :, 1]
B = rgb_array[:, :, 2]

# Define the degree of the polynomial
deg = 2

# Define the x and y values for the polynomial fit
x = np.arange(img.size[0])
y = np.arange(img.size[1])

# Fit a 2D polynomial to the R channel
R_coeffs = np.polyfit(x, y[:, np.newaxis], deg)
R_poly = np.polyval(R_coeffs, x)

# Fit a 2D polynomial to the G channel
G_coeffs = np.polyfit(x, y[:, np.newaxis], deg)
G_poly = np.polyval(G_coeffs, x)

# Fit a 2D polynomial to the B channel
B_coeffs = np.polyfit(x, y[:, np.newaxis], deg)
B_poly = np.polyval(B_coeffs, x)

# Combine the polynomial fits into a single feature vector
features = np.hstack((R_poly.ravel(), G_poly.ravel(), B_poly.ravel()))

# Plot the original image and the polynomial approximation
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img)
axs[0].set_title('Original Image')
axs[1].imshow(np.dstack((R_poly, G_poly, B_poly)))
axs[1].set_title('Polynomial Approximation')
plt.show()
