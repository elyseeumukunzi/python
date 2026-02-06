"""
Bulk Background Removal Tool
Removes backgrounds from profile images and exports as transparent PNGs
"""

import os
from pathlib import Path
from PIL import Image
from rembg import remove
from typing import List, Tuple

# Configuration
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
MAX_SIZE = 500  # Maximum width/height in pixels
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.webp'}


def create_output_folder(output_path: Path) -> None:
    """Create output folder if it doesn't exist"""
    output_path.mkdir(parents=True, exist_ok=True)
    print(f"✓ Output folder ready: {output_path}\n")


def get_image_files(input_path: Path) -> List[Path]:
    """Get all supported image files from input folder"""
    if not input_path.exists():
        raise FileNotFoundError(f"Input folder not found: {input_path}")
    
    image_files = [
        f for f in input_path.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_FORMATS
    ]
    
    return sorted(image_files)


def resize_image(image: Image.Image, max_size: int) -> Image.Image:
    """
    Resize image to fit within max_size while maintaining aspect ratio
    """
    width, height = image.size
    
    # Check if resizing is needed
    if width <= max_size and height <= max_size:
        return image
    
    # Calculate new dimensions
    if width > height:
        new_width = max_size
        new_height = int((max_size / width) * height)
    else:
        new_height = max_size
        new_width = int((max_size / height) * width)
    
    # Use LANCZOS for high-quality downsampling
    return image.resize((new_width, new_height), Image.Resampling.LANCZOS)


def process_image(input_file: Path, output_path: Path, max_size: int) -> Tuple[bool, str]:
    """
    Process a single image: remove background, resize, and save as PNG
    
    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Read input image
        with open(input_file, 'rb') as f:
            input_data = f.read()
        
        # Remove background
        output_data = remove(input_data)
        
        # Open as PIL Image
        image = Image.open(io.BytesIO(output_data))
        
        # Resize if needed
        image = resize_image(image, max_size)
        
        # Prepare output filename
        output_filename = input_file.stem + '.png'
        output_file = output_path / output_filename
        
        # Save as PNG with transparency
        image.save(output_file, 'PNG', optimize=True)
        
        return True, f"Completed: {output_filename}"
        
    except Exception as e:
        return False, f"Failed: {input_file.name} - {str(e)}"


def main():
    """Main execution function"""
    print("=" * 60)
    print("BULK BACKGROUND REMOVAL TOOL")
    print("=" * 60)
    print()
    
    # Setup paths
    input_path = Path(INPUT_FOLDER)
    output_path = Path(OUTPUT_FOLDER)
    
    # Create output folder
    try:
        create_output_folder(output_path)
    except Exception as e:
        print(f"✗ Error creating output folder: {e}")
        return
    
    # Get image files
    try:
        image_files = get_image_files(input_path)
    except FileNotFoundError as e:
        print(f"✗ {e}")
        print(f"  Please create the '{INPUT_FOLDER}' folder and add your images.")
        return
    
    if not image_files:
        print(f"✗ No images found in '{INPUT_FOLDER}'")
        print(f"  Supported formats: {', '.join(SUPPORTED_FORMATS)}")
        return
    
    print(f"Found {len(image_files)} image(s) to process")
    print(f"Max size: {MAX_SIZE}x{MAX_SIZE}px")
    print()
    
    # Process images
    success_count = 0
    failed_files = []
    
    for idx, image_file in enumerate(image_files, 1):
        print(f"[{idx}/{len(image_files)}] Processing: {image_file.name}")
        
        success, message = process_image(image_file, output_path, MAX_SIZE)
        
        if success:
            print(f"    ✓ {message}")
            success_count += 1
        else:
            print(f"    ✗ {message}")
            failed_files.append(image_file.name)
    
    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total processed: {len(image_files)}")
    print(f"Successful: {success_count}")
    print(f"Failed: {len(failed_files)}")
    
    if failed_files:
        print("\nFailed files:")
        for filename in failed_files:
            print(f"  - {filename}")
    
    print(f"\n✓ Output saved to: {output_path.absolute()}")
    print()


if __name__ == "__main__":
    import io  # Import here to avoid issues if not needed
    main()
