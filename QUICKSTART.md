# Quick Start Guide

## Installation (One-Time Setup)

```cmd
pip install "rembg[cpu]" pillow
```

**Note:** First run will download AI model (~176MB) - this only happens once.

## Usage (3 Simple Steps)

### 1. Add Your Images
Place your profile photos in the `input_images` folder

### 2. Run the Script
```cmd
python remove_bg.py
```

### 3. Get Results
Find your transparent PNGs in the `output_images` folder

## What It Does

✅ Removes backgrounds automatically  
✅ Resizes to 500x500px max (keeps aspect ratio)  
✅ Saves as transparent PNG  
✅ Optimizes file size  
✅ Shows progress for each image

## Example Output

```
============================================================
BULK BACKGROUND REMOVAL TOOL
============================================================

✓ Output folder ready: output_images

Found 25 image(s) to process
Max size: 500x500px

[1/25] Processing: john_doe.jpg
    ✓ Completed: john_doe.png
[2/25] Processing: jane_smith.png
    ✓ Completed: jane_smith.png
...

============================================================
SUMMARY
============================================================
Total processed: 25
Successful: 25
Failed: 0

✓ Output saved to: C:\xampp\htdocs\python\output_images
```

## Customization

Edit these values in `remove_bg.py`:

```python
INPUT_FOLDER = "input_images"   # Change input folder
OUTPUT_FOLDER = "output_images" # Change output folder
MAX_SIZE = 500                  # Change max dimensions
```

## Troubleshooting

**"No images found"**
- Make sure images are in `input_images` folder
- Check file format (JPG, JPEG, PNG, WEBP only)

**Slow processing?**
- First run downloads model (one-time, ~30 seconds)
- Normal speed: 2-5 seconds per image on CPU

**Need faster processing?**
- Install GPU version: `pip install "rembg[gpu]"`
- Requires NVIDIA GPU with CUDA

## That's It!

You're ready to process hundreds of profile images automatically.
