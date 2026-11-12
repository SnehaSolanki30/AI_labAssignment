import time
import math

# ==========================================================
# PROBLEM STATEMENT:
# Implement 2D Image Convolution with Sobel Edge Detection 
# kernels (Gx and Gy) on a grayscale pixel matrix to detect 
# object boundaries in Computer Vision.
# ==========================================================

def sobel_edge_detection(image):
    """Applies 3x3 Sobel X and Y filters to compute edge gradient magnitudes."""
    start_time = time.time()
    rows = len(image)
    cols = len(image[0])

    # Sobel Kernels for horizontal and vertical edges
    Gx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    Gy = [[-1, -2, -1],
          [ 0,  0,  0],
          [ 1,  2,  1]]

    edge_map = [[0] * cols for _ in range(rows)]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            sum_x = 0
            sum_y = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    pixel = image[r + i][c + j]
                    sum_x += pixel * Gx[i + 1][j + 1]
                    sum_y += pixel * Gy[i + 1][j + 1]

            magnitude = int(math.sqrt(sum_x ** 2 + sum_y ** 2))
            edge_map[r][c] = min(255, magnitude)

    exec_time = (time.time() - start_time) * 1000
    return edge_map, exec_time


if __name__ == "__main__":
    # 6x6 Sample Grayscale Image (Dark background 10, Bright object 200 on right half)
    grayscale_image = [
        [10, 10, 10, 200, 200, 200],
        [10, 10, 10, 200, 200, 200],
        [10, 10, 10, 200, 200, 200],
        [10, 10, 10, 200, 200, 200],
        [10, 10, 10, 200, 200, 200],
        [10, 10, 10, 200, 200, 200]
    ]

    edges, elapsed = sobel_edge_detection(grayscale_image)

    print("=== Computer Vision: Sobel Edge Detection ===")
    print("Input Grayscale Pixel Matrix:")
    for row in grayscale_image:
        print("  ", [f"{val:3d}" for val in row])

    print("\nDetected Edge Gradient Map (High values = Strong Edge):")
    for row in edges:
        print("  ", [f"{val:3d}" for val in row])

    print(f"\nExecution Time: {elapsed:.4f} ms")
