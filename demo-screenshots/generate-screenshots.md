# How to Generate Professional Screenshots

## Method 1: Browser Screenshot
1. Open the HTML files in Chrome/Firefox
2. Press `F12` for Developer Tools
3. Toggle Device Toolbar (📱 icon)
4. Set dimensions to 1920x1080 or 1200x800
5. Right-click → "Capture screenshot"

## Method 2: Command Line (if you have node)
```bash
# Install screenshot tool
npm install -g pageres-cli

# Generate screenshots
pageres demo-screenshots/dashboard-mockup.html 1920x1080 --filename="dashboard"
pageres demo-screenshots/architecture-mockup.html 1920x1080 --filename="architecture"
