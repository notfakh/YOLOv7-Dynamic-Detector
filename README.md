# YOLOv7-Dynamic-Detector
Runs YOLOv7 object detection by dynamically loading the detect module, configuring custom arguments, and processing an input image to generate detection outputs saved in organized result folders.

## 📋 Project Overview

This project provides a simple interface to run YOLOv7 (You Only Look Once version 7) object detection on images. It dynamically loads the official YOLOv7 implementation and configures detection parameters through an easy-to-use Python script.

## 🎯 What Does This Do?

- **Detects** 80 different object classes (COCO dataset)
- **Processes** single images or batches
- **Saves** detection results with bounding boxes
- **Exports** text files with coordinates and confidence scores
- **Configures** detection parameters (confidence, IoU threshold)
- **Uses** pre-trained YOLOv7 weights
- **Supports** GPU acceleration for faster inference

## 🔑 Key Features

- ✅ Simple wrapper for YOLOv7 detection
- ✅ Customizable confidence and IoU thresholds
- ✅ Automatic result saving (images + text labels)
- ✅ GPU/CPU support
- ✅ Confidence scores in output files
- ✅ Class-specific or all-class detection
- ✅ Non-Maximum Suppression (NMS)

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.7+
CUDA (optional, for GPU acceleration)
```

### Installation

1. Clone YOLOv7 repository:
```bash
git clone https://github.com/WongKinYiu/yolov7.git
cd yolov7
pip install -r requirements.txt
```

2. Download YOLOv7 weights:
```bash
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
```

3. Clone this wrapper repository:
```bash
git clone https://github.com/notfakh/yolov7-detection-wrapper.git
cd yolov7-detection-wrapper
```

4. Install additional requirements:
```bash
pip install -r requirements.txt
```

### Project Structure

```
project/
│
├── yolov7/                          # YOLOv7 official repository
│   ├── detect.py
│   ├── yolov7.pt                   # Pre-trained weights
│   └── runs/detect/exp/            # Output directory
│
├── yolov7_detector.py              # This wrapper script
├── sport.jpg                       # Input image
└── requirements.txt
```

### Usage

1. Update paths in the script:
```python
yolov7_path = "path/to/yolov7"      # YOLOv7 directory
source = "path/to/your/image.jpg"   # Input image
```

2. Run detection:
```bash
python yolov7_detector.py
```

**Output:**
```
Running YOLOv7 detection...
YOLOv7 detection completed.
Results saved in: C:/pythonProject/yolov7/runs/detect/exp
```

## 📊 Detection Parameters

### Core Configuration:

```python
opt = Namespace(
    weights="yolov7.pt",     # Model weights
    source="image.jpg",       # Input image/video/directory
    img_size=640,            # Inference size (pixels)
    conf_thres=0.25,         # Confidence threshold (0.0-1.0)
    iou_thres=0.45,          # IoU threshold for NMS
    device='',               # '' = auto, '0' = GPU, 'cpu' = CPU
    save_txt=True,           # Save results to .txt
    save_conf=True,          # Include confidence in .txt
    nosave=False,            # Save output images
    classes=None,            # Filter by class (None = all)
    agnostic_nms=False,      # Class-agnostic NMS
    augment=False,           # Augmented inference
)
```

### Parameter Explanations:

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| **conf_thres** | Minimum confidence to detect | 0.25 | 0.0-1.0 |
| **iou_thres** | IoU threshold for NMS | 0.45 | 0.0-1.0 |
| **img_size** | Input image size | 640 | 320-1280 |
| **device** | Computation device | auto | '', '0', 'cpu' |
| **classes** | Specific classes to detect | None | 0-79 or None |

## 🎨 COCO Dataset Classes (80 Classes)

YOLOv7 detects these object categories:

| Category | Classes |
|----------|---------|
| **Person** | person |
| **Vehicles** | bicycle, car, motorcycle, airplane, bus, train, truck, boat |
| **Animals** | bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe |
| **Accessories** | backpack, umbrella, handbag, tie, suitcase |
| **Sports** | frisbee, skis, snowboard, sports ball, kite, baseball bat, glove, skateboard, surfboard, tennis racket |
| **Kitchen** | bottle, wine glass, cup, fork, knife, spoon, bowl |
| **Food** | banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake |
| **Furniture** | chair, couch, potted plant, bed, dining table, toilet |
| **Electronics** | tv, laptop, mouse, remote, keyboard, cell phone |
| **Appliances** | microwave, oven, toaster, sink, refrigerator |
| **Indoor** | book, clock, vase, scissors, teddy bear, hair drier, toothbrush |

**Full list**: See [COCO classes](https://github.com/WongKinYiu/yolov7/blob/main/data/coco.yaml)

## 📈 Output Format

### Saved Files:

1. **Image with Bounding Boxes**
   - Location: `runs/detect/exp/image.jpg`
   - Visual representation with boxes and labels

2. **Text Labels**
   - Location: `runs/detect/exp/labels/image.txt`
   - Format: `class_id x_center y_center width height confidence`
   - Normalized coordinates (0.0-1.0)

### Example Label File:
```
0 0.5 0.5 0.3 0.4 0.92    # person at center, 92% confidence
2 0.2 0.3 0.15 0.2 0.87   # car, 87% confidence
```

## 🛠️ Customization

### Detect Specific Classes Only

```python
# Detect only people (class 0) and cars (class 2)
opt.classes = [0, 2]
```

### Adjust Detection Sensitivity

```python
# More sensitive (detect more objects, more false positives)
opt.conf_thres = 0.15
opt.iou_thres = 0.5

# Less sensitive (fewer detections, more accurate)
opt.conf_thres = 0.5
opt.iou_thres = 0.3
```

### Process Video or Multiple Images

```python
# Video file
opt.source = "video.mp4"

# Directory of images
opt.source = "images/"

# Webcam
opt.source = "0"
```

### Change Output Directory

```python
opt.project = "custom_output"
opt.name = "my_detection"
# Results will be saved in: custom_output/my_detection/
```

### Enable GPU

```python
# Use first GPU
opt.device = '0'

# Use specific GPU
opt.device = '1'

# Force CPU
opt.device = 'cpu'
```

### Higher Resolution Processing

```python
# Better accuracy, slower processing
opt.img_size = 1280

# Faster processing, lower accuracy
opt.img_size = 416
```

## 💡 Use Cases

- **Surveillance**: Detect people and vehicles in security footage
- **Sports Analysis**: Track players and equipment
- **Retail**: Count products and customers
- **Traffic Monitoring**: Vehicle counting and classification
- **Wildlife**: Animal detection in camera traps
- **Safety**: PPE detection (hard hats, vests)
- **Autonomous Vehicles**: Object detection for navigation

## 🔬 Extending the Project

Ideas for enhancement:

1. **Batch Processing**
   ```python
   import glob
   for image in glob.glob("images/*.jpg"):
       opt.source = image
       detect_module.detect()
   ```

2. **Real-time Webcam**
   ```python
   opt.source = "0"  # Webcam
   opt.view_img = True  # Display results
   ```

3. **Count Objects**
   ```python
   # Parse results from label files
   with open(label_file) as f:
       detections = len(f.readlines())
   print(f"Detected {detections} objects")
   ```

4. **Filter by Confidence**
   ```python
   # Only keep high-confidence detections
   def filter_detections(label_file, min_conf=0.8):
       with open(label_file) as f:
           lines = [l for l in f if float(l.split()[-1]) >= min_conf]
   ```

5. **Draw Custom Boxes**
   ```python
   import cv2
   img = cv2.imread('result.jpg')
   # Read labels and draw custom boxes
   ```

6. **API Endpoint**
   ```python
   from flask import Flask, request
   
   @app.route('/detect', methods=['POST'])
   def detect_api():
       # Save uploaded image
       # Run detection
       # Return results
   ```

7. **Tracking Integration**
   ```python
   # Add object tracking across frames
   from deep_sort import DeepSort
   tracker = DeepSort()
   ```

## 📊 Performance Benchmarks

### YOLOv7 Models:

| Model | Size | mAP@50 | FPS (V100) | Parameters |
|-------|------|--------|------------|------------|
| YOLOv7-tiny | 6.2MB | 38.7% | 286 | 6.2M |
| YOLOv7 | 74.8MB | 51.4% | 161 | 36.9M |
| YOLOv7-X | 142.1MB | 53.1% | 114 | 71.3M |

**mAP**: Mean Average Precision on COCO dataset  
**FPS**: Frames per second (higher is better)

## 🤝 Contributing

Contributions welcome! Enhancement ideas:

- Add GUI interface with Tkinter/PyQt
- Implement object tracking
- Add video processing pipeline
- Create REST API wrapper
- Add custom class training guide
- Implement multi-GPU support
- Add performance profiling
- Create Docker container

## 👤 Author

**Fakhrul Sufian**
- GitHub: [@notfakh](https://github.com/notfakh)
- LinkedIn: [Fakhrul Sufian](https://www.linkedin.com/in/fakhrul-sufian-b51454363/)
- Email: fkhrlnasry@gmail.com

## 🙏 Acknowledgments

- YOLOv7 authors (Chien-Yao Wang, Alexey Bochkovskiy, Hong-Yuan Mark Liao)
- Official YOLOv7 repository maintainers
- COCO dataset creators
- PyTorch and OpenCV communities

## 📚 References

- [YOLOv7 Paper](https://arxiv.org/abs/2207.02696)
- [Official YOLOv7 Repository](https://github.com/WongKinYiu/yolov7)
- [COCO Dataset](https://cocodataset.org/)
- [YOLO Object Detection](https://pjreddie.com/darknet/yolo/)

## 🐛 Troubleshooting

**Issue: Module not found**
- Ensure YOLOv7 path is correct
- Check `sys.path.append()` points to right directory
- Verify `detect.py` exists in YOLOv7 folder

**Issue: Weights not found**
- Download `yolov7.pt` from official releases
- Update `weights` path in script
- Check file permissions

**Issue: CUDA out of memory**
- Reduce `img_size` (try 416 or 320)
- Use `device='cpu'` to force CPU
- Process images one at a time

**Issue: Low detection accuracy**
- Increase `img_size` to 1280
- Lower `conf_thres` to 0.15
- Ensure good image quality
- Check if objects are in COCO classes

**Issue: Too many false detections**
- Increase `conf_thres` to 0.5
- Lower `iou_thres` to 0.3
- Filter by specific classes

**Issue: Slow processing**
- Enable GPU with `device='0'`
- Reduce `img_size`
- Use YOLOv7-tiny for speed
- Disable `augment=True`

## 📧 Contact

For questions, suggestions, or collaboration:
- Open an issue in this repository
- Email: fkhrlnasry@gmail.com
- Connect on LinkedIn

---

⭐ If this project helped you with object detection, please give it a star!

## 🎓 Learning Outcomes

After working through this project, you'll understand:
- YOLO object detection architecture
- Python module dynamic loading
- Detection parameter tuning
- Non-Maximum Suppression (NMS)
- Confidence thresholds and IoU
- Bounding box coordinate systems
- GPU vs CPU inference trade-offs

**Perfect for:** Computer vision students, ML engineers, and anyone interested in real-time object detection!
