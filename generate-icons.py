"""
Generate PWA icons for Bunker Calculator PRO
This script creates all required icon sizes for iOS and Android PWA
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Icon sizes needed for PWA
ICON_SIZES = [16, 32, 72, 96, 128, 144, 152, 167, 180, 192, 384, 512]

# Colors matching the app theme
BG_COLOR = '#0043ce'  # IBM Blue 60
TEXT_COLOR = '#ffffff'  # White

def create_icon(size):
    """Create a single icon of specified size"""
    # Create image with blue background
    img = Image.new('RGB', (size, size), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Calculate font size (proportional to icon size)
    font_size = int(size * 0.5)
    
    try:
        # Try to use a nice font if available
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Draw "BC" text in center
    text = "BC"
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center text
    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]
    
    # Draw text
    draw.text((x, y), text, fill=TEXT_COLOR, font=font)
    
    # Add rounded corners for iOS style
    if size >= 128:
        mask = Image.new('L', (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        corner_radius = int(size * 0.2)  # 20% corner radius
        mask_draw.rounded_rectangle([(0, 0), (size, size)], corner_radius, fill=255)
        
        # Apply mask
        output = Image.new('RGB', (size, size), BG_COLOR)
        output.paste(img, (0, 0))
        output.putalpha(mask)
        return output
    
    return img

def main():
    """Generate all icon sizes"""
    print("🎨 Generating PWA icons for Bunker Calculator PRO...")
    
    # Create icons directory if it doesn't exist
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    for size in ICON_SIZES:
        filename = f"icon-{size}.png"
        filepath = os.path.join(script_dir, filename)
        
        print(f"  Creating {filename}...")
        icon = create_icon(size)
        icon.save(filepath, 'PNG', optimize=True)
    
    print("✅ All icons generated successfully!")
    print("\n📱 Icons created:")
    for size in ICON_SIZES:
        print(f"  - icon-{size}.png")
    
    print("\n🚀 Next steps:")
    print("  1. Open 'bunker-calculator (1).html' in a browser")
    print("  2. On iPhone: Tap Share → Add to Home Screen")
    print("  3. The app will install as a native-like application")
    print("\n💡 The app will work offline and look like a native iOS app!")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("❌ Error: PIL (Pillow) library not found")
        print("📦 Install it with: pip install Pillow")
        print("\nOr run: python -m pip install Pillow")