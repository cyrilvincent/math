import skimage as ski

image = ski.data.coins()
# ... or any other NumPy array!
edges = ski.filters.sobel(image)
ski.io.imshow(edges)
ski.io.show()
