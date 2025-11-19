import os
import sys
import importlib.util
from argparse import Namespace

# Add the YOLOv7 directory to the system path
yolov7_path = "C:\pythonProject\yolov7"
sys.path.append(yolov7_path)

# Dynamically load detect.py
detect_path = os.path.join(yolov7_path, "detect.py")
spec = importlib.util.spec_from_file_location("detect", detect_path)
detect_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(detect_module)

# Define the arguments expected by the detect() function
opt = Namespace(
    weights=os.path.join(yolov7_path, "yolov7.pt"),  # Path to YOLOv7 weights
    source="C:\pythonProject/sport.jpg",  # Input image
    img_size=640,         # Inference image size
    conf_thres=0.25,      # Confidence threshold
    iou_thres=0.45,       # IoU threshold for NMS
    device='',            # Use GPU if available, otherwise CPU
    view_img=False,       # Don't display results
    save_txt=True,        # Save detection results to a .txt file
    save_conf=True,       # Save confidence scores in .txt labels
    nosave=False,         # Save images/videos with detections
    classes=None,         # Detect all classes
    agnostic_nms=False,   # Class-agnostic NMS
    augment=False,        # No augmented inference
    update=False,         # Don't update all models
    project=os.path.join(yolov7_path, "runs/detect"),  # Output directory for results
    name="exp",           # Subdirectory name for this run
    exist_ok=True,        # Don't increment directory name
    no_trace=True         # Disable tracing
)

# Inject opt as a global variable into the detect module
detect_module.opt = opt

# Run the detection
print("Running YOLOv7 detection...")
detect_module.detect()  # Call the detect function
print("YOLOv7 detection completed.")

# Optionally display or process results here
output_dir = os.path.join(opt.project, opt.name)
print(f"Results saved in: {output_dir}")