import numpy as np

rnd = (np.random.rand(1000000) - 0.5) * 2
print(np.mean(rnd), np.std(rnd))
print(np.median(rnd), np.quantile(rnd, [0.01, 0.1, 0.25, 0.5, 0.75]))

# luminance d'une image (mean)
# contraste d'une image (std)
# black_white (mean sur la 3ème dimension)
# profile vertical d'une image n&b
# auto_lum => ramène la luminance à 255/2, np.clip(array, 0, 255)
# bonus auto_lum_contrast, le contraste ideal est 255/4

