# Examples & Use Cases

## Basic Usage Example

```bash
# 1. Add images to input folder
cp ~/photos/*.jpg input_images/

# 2. Run the script
python remove_bg.py

# 3. Check results
ls output_images/
```

## Output Example

```
============================================================
BULK BACKGROUND REMOVAL TOOL
============================================================

✓ Output folder ready: output_images

Found 10 image(s) to process
Max size: 500x500px

[1/10] Processing: profile_001.jpg
    ✓ Completed: profile_001.png
[2/10] Processing: profile_002.jpg
    ✓ Completed: profile_002.png
[3/10] Processing: profile_003.png
    ✓ Completed: profile_003.png
...

============================================================
SUMMARY
============================================================
Total processed: 10
Successful: 10
Failed: 0

✓ Output saved to: C:\path\to\output_images
```

## Real-World Use Cases

### 1. E-commerce Product Photos

```python
# Customize for product images
INPUT_FOLDER = "products"
OUTPUT_FOLDER = "products_transparent"
MAX_SIZE = 1000  # Larger for product detail
```

### 2. Team Member Directory

```python
# Optimize for profile photos
INPUT_FOLDER = "team_photos"
OUTPUT_FOLDER = "team_profiles"
MAX_SIZE = 300  # Smaller for web profiles
```

### 3. Social Media Avatars

```python
# Square avatars
INPUT_FOLDER = "avatars"
OUTPUT_FOLDER = "avatars_processed"
MAX_SIZE = 400  # Standard avatar size
```

## Before & After

### Input
- Format: JPG with background
- Size: 2400x3200px
- File size: 2.5MB

### Output
- Format: PNG with transparency
- Size: 375x500px (aspect ratio maintained)
- File size: 180KB (optimized)

## Performance Benchmarks

| Batch Size | CPU Time | GPU Time |
|-----------|----------|----------|
| 10 images | ~30 sec  | ~8 sec   |
| 50 images | ~2.5 min | ~40 sec  |
| 100 images| ~5 min   | ~1.5 min |
| 500 images| ~25 min  | ~7 min   |

*Times are approximate and vary based on hardware and image complexity*

## Tips for Best Results

1. **Image Quality**
   - Use high-resolution source images
   - Ensure good lighting in original photos
   - Clear subject-background separation works best

2. **Batch Processing**
   - Process similar images together
   - Use consistent naming conventions
   - Keep backups of originals

3. **Performance**
   - Close unnecessary applications
   - Process during off-peak hours for large batches
   - Consider GPU acceleration for 100+ images

## Common Workflows

### Workflow 1: Quick Profile Photo Batch
```bash
# Add photos
cp ~/Downloads/team_photos/* input_images/

# Process
python remove_bg.py

# Upload to system
cp output_images/* ~/web_project/public/profiles/
```

### Workflow 2: Product Catalog
```bash
# Organize by category
mkdir input_images/electronics
mkdir input_images/clothing

# Process each category
python remove_bg.py

# Review and approve
open output_images/
```

### Workflow 3: Automated Pipeline
```bash
# Watch folder and auto-process (advanced)
# Requires additional scripting
while true; do
    if [ "$(ls -A input_images)" ]; then
        python remove_bg.py
        mv input_images/* processed/
    fi
    sleep 60
done
```
