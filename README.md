# 🎨 Bulk Background Remover

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![rembg](https://img.shields.io/badge/powered%20by-rembg-green.svg)](https://github.com/danielgatis/rembg)

A powerful, offline AI tool for automatically removing backgrounds from images in bulk. Perfect for profile photos, product images, and any scenario requiring transparent backgrounds.

## ✨ Features

- 🤖 **Offline AI Processing** - No API keys, no internet required after setup
- ⚡ **Batch Processing** - Process hundreds of images automatically
- 🎯 **Smart Resizing** - Maintains aspect ratio while optimizing dimensions
- 🖼️ **Transparent PNGs** - Professional-quality output
- 🛡️ **Error Handling** - Skips corrupted files, continues processing
- 📊 **Progress Tracking** - Real-time status updates
- 🎨 **Production Ready** - Clean, modular, well-documented code

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/bulk-background-remover.git
cd bulk-background-remover

# Install dependencies
pip install -r requirements.txt
```

**Note:** First run will download the AI model (~176MB) automatically. This only happens once.

### Usage

```bash
# 1. Add your images to input_images folder
# 2. Run the script
python remove_bg.py

# Windows users can also double-click run.bat
```

That's it! Find your processed images in the `output_images` folder.

## 📋 Requirements

- Python 3.10 or higher
- 4GB RAM minimum (8GB recommended for large batches)
- ~200MB disk space for AI model

## 🎯 Use Cases

Perfect for:
- 👤 Profile photos for member directories
- 🛍️ E-commerce product images
- 📱 App/website avatars
- 🎨 Graphic design workflows
- 📊 Presentation materials
- 🖼️ Any project requiring transparent backgrounds

## 📁 Project Structure

```
bulk-background-remover/
├── input_images/          # Place your images here
├── output_images/         # Processed images appear here
├── remove_bg.py          # Main script
├── run.bat               # Windows quick-run script
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── QUICKSTART.md        # Quick reference guide
```

## ⚙️ Configuration

Customize settings in `remove_bg.py`:

```python
INPUT_FOLDER = "input_images"   # Input folder name
OUTPUT_FOLDER = "output_images" # Output folder name
MAX_SIZE = 500                  # Maximum width/height in pixels
```

## 📊 Supported Formats

**Input:** JPG, JPEG, PNG, WEBP  
**Output:** PNG with transparency

## 🎨 Output Specifications

- Format: PNG with alpha channel
- Max dimensions: 500x500px (configurable)
- Aspect ratio: Preserved
- File size: Optimized
- Filename: Original name + `.png` extension

## 🚀 Performance

| Mode | Speed per Image | Requirements |
|------|----------------|--------------|
| CPU  | 2-5 seconds    | Any system   |
| GPU  | 0.5-1 second   | NVIDIA CUDA  |

**First run:** +30 seconds (one-time model download)

## 🔧 Advanced Options

### GPU Acceleration

For faster processing with NVIDIA GPU:

```bash
pip install "rembg[gpu]"
```

Requires CUDA-compatible GPU and drivers.

### Custom Batch Size

Process images in smaller batches if memory is limited:

```python
# Process 50 images at a time
for batch in chunks(image_files, 50):
    process_batch(batch)
```

## 🐛 Troubleshooting

<details>
<summary><b>"No images found"</b></summary>

- Ensure images are in the `input_images` folder
- Check file extensions (must be .jpg, .jpeg, .png, or .webp)
- Verify folder permissions
</details>

<details>
<summary><b>"Module not found"</b></summary>

```bash
pip install --upgrade -r requirements.txt
```
</details>

<details>
<summary><b>Slow processing</b></summary>

- First run downloads the AI model (one-time, ~30 seconds)
- Normal CPU speed: 2-5 seconds per image
- Consider GPU acceleration for large batches
</details>

<details>
<summary><b>Memory issues</b></summary>

- Process in smaller batches (50-100 images)
- Close other applications
- Reduce MAX_SIZE in configuration
</details>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](#) file for details.

## 🙏 Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) - The amazing AI background removal library
- [Pillow](https://python-pillow.org/) - Python Imaging Library

## 📧 Support

- 🐛 [Report a bug](https://github.com/yourusername/bulk-background-remover/issues)
- 💡 [Request a feature](https://github.com/yourusername/bulk-background-remover/issues)
- 📖 [Documentation](https://github.com/yourusername/bulk-background-remover/wiki)

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

Made with ❤️ for the open-source community
