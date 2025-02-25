import cv2

def count_sunspots (image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print ("Error: Could not load image.")
        return 0

# Threshold to detect dark skpots (sunspots)
_, thresholded = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY_INV)

# FInd sunpots (Connected Components)
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# OCunt sunports
sunspots_count = len(contours)

print(f"Number of sunspots detected: {sunpots_count}")
return sunspot_count

#Get the path to the solar image
image_path = input("/home/dell/PythonProjects/Sun.jpeg")
count_sunspots(image_path)
