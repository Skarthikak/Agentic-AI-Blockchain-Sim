#!/usr/bin/env python3
"""
Generate placeholder screenshots for the Agentic AI Blockchain Simulator
Run this script to create placeholder PNG files that can be replaced with real screenshots later.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_screenshot(text, filename, width=1200, height=800):
    """Create a placeholder screenshot with descriptive text"""
    
    # Create image with dark background
    img = Image.new('RGB', (width, height), color=(26, 32, 44))
    draw = ImageDraw.Draw(img)
    
    # Add border
    draw.rectangle([0, 0, width-1, height-1], outline=(49, 130, 206), width=4)
    
    # Add title
    try:
        # Try to use a larger font if available
        title_font = ImageFont.truetype("Arial", 40)
        text_font = ImageFont.truetype("Arial", 24)
    except:
        # Fallback to default font
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Project title
    draw.text((width//2, 100), "🤖 Agentic AI Blockchain Simulator", 
              fill=(99, 179, 237), font=title_font, anchor="mm")
    
    # Screenshot description
    draw.text((width//2, height//2 - 50), text, 
              fill(255, 255, 255), font=text_font, anchor="mm")
    
    # Instruction text
    draw.text((width//2, height//2 + 50), "Placeholder - Replace with actual screenshot", 
              fill(160, 174, 192), font=text_font, anchor="mm")
    
    # Save the image
    os.makedirs('demo-screenshots', exist_ok=True)
    img.save(f'demo-screenshots/{filename}')
    print(f"✅ Created placeholder: demo-screenshots/{filename}")

def main():
    """Generate all placeholder screenshots"""
    
    screenshots = [
        {
            "text": "Dashboard Overview - Real-time agent performance monitoring",
            "filename": "dashboard.png"
        },
        {
            "text": "System Architecture - Multi-agent coordination diagram", 
            "filename": "architecture.png"
        },
        {
            "text": "Agent Activity Feed - Live transaction and prediction tracking",
            "filename": "activity-feed.png"
        },
        {
            "text": "Prediction Market - AI agent performance in markets",
            "filename": "prediction-market.png"
        }
    ]
    
    print("🖼️ Generating placeholder screenshots...")
    
    for screenshot in screenshots:
        create_placeholder_screenshot(screenshot["text"], screenshot["filename"])
    
    print("🎉 Placeholder screenshots generated!")
    print("📝 Replace these with actual screenshots when available")

if __name__ == "__main__":
    main()
