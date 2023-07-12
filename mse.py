import numpy as np
from PIL import Image

# Load cover and stego images
cover_image = np.array(Image.open('num1.png'))
stego_image = np.array(Image.open('1_1.png'))

# Calculate MSE
mse = np.mean((cover_image - stego_image)**2)

# Print MSE
print('MSE:', mse)

