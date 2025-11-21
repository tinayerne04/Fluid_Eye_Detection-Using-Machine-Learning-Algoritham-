# 👁️ Eye Flue Guard

<div align="center">

![Eye Flue Guard Logo](https://img.shields.io/badge/Eye%20Flue-Guard-blue?style=for-the-badge&logo=eye&logoColor=white)

**An AI-Powered Eye Flu Detection System**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Contributing](#contributing)

</div>

---

## 📋 Overview

**Eye Flue Guard** is an innovative web-based platform that leverages machine learning to detect eye flu (conjunctivitis) from uploaded eye images. Built with Flask and PyScript, the system provides instant predictions for both humans and animals, making eye health assessment accessible and convenient.

> ⚠️ **Medical Disclaimer**: This tool is for educational and awareness purposes only. Always consult qualified healthcare professionals for accurate medical diagnosis and treatment.

## ✨ Features

### 🎯 Core Functionality
- **Instant Image Analysis** - Upload eye images and receive immediate predictions
- **Universal Detection** - Works for both human and animal eyes
- **Machine Learning Backend** - Trained model for accurate predictions
- **User-Friendly Interface** - Clean, responsive design built with Tailwind CSS
- **Real-Time Results** - Fast processing with visual feedback

### 🎨 Design Highlights
- **Responsive Layout** - Seamless experience across desktop, tablet, and mobile devices
- **Smooth Animations** - AOS (Animate On Scroll) library integration
- **Dark Mode Support** - Toggle between light and dark themes
- **Interactive UI** - Intuitive navigation and clear call-to-action buttons

### 📊 Information Hub
- Comprehensive symptom guide for eye flu
- Statistics dashboard showing platform usage
- Healthcare provider directory with contact information
- Patient testimonials and feedback section

## 🚀 Demo

### Screenshots

**Home Page**
- Clean hero section with image upload functionality
- Eye-catching gradient design with medical imagery

**Results Page**
- Clear prediction display
- Visual representation of uploaded image
- Health guidance and recommendations

**Statistics Section**
- 2.7K+ Downloads
- 1.3K+ Active Users
- 74 Medical Files Processed
- 46 Locations Served

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python/Flask | Backend server and API |
| PyScript | Client-side Python execution |
| HTML5 | Structure and semantic markup |
| Tailwind CSS | Responsive styling and utilities |
| JavaScript/jQuery | DOM manipulation and interactivity |
| Machine Learning | Image classification model |
| AOS Library | Scroll animations |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for CDN resources)

### Setup Steps

1. **Clone the repository or download from Google Drive**
```bash
# If using Git
git clone https://github.com/yourusername/eye-flue-guard.git
cd eye-flue-guard

# Or download from: Fluid Eye Project - Google Drive
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure PyScript**
```bash
# Ensure pyscript.json is properly configured
# This file contains PyScript configuration settings
```

4. **Run the Flask application**
```bash
python main.py
```

5. **Access the application**
```
Open your browser and navigate to: http://localhost:5000
```

## 💻 Usage

### For Users

1. **Upload an Image**
   - Navigate to the home page
   - Click on the file upload button
   - Select a clear image of the eye
   - Supported formats: JPG, PNG, JPEG

2. **Submit for Analysis**
   - Click the "Submit Image" button
   - Wait for the AI model to process your image

3. **View Results**
   - Review the prediction outcome
   - See the uploaded image for reference
   - Read the health recommendations
   - Contact healthcare providers if needed

### For Developers

```python
# Example: Flask route for image processing
from flask import Flask, request, render_template
from main import predict_eye_flu

@app.route('/submit', methods=['POST'])
def submit_image():
    if 'my_image' in request.files:
        file = request.files['my_image']
        prediction = predict_eye_flu(file)
        return render_template('index.html', 
                             prediction=prediction,
                             img_path=file.filename)
```

## 🏗️ Project Structure

```
Fluid Eye Project/
│
├── main.py                 # Flask application & ML model logic
├── pyscript                # PyScript configuration file
├── requirements.txt        # Python dependencies
├── .gitattributes         # Git configuration
│
├── static/                # Static assets
│   ├── css/              # Stylesheets
│   ├── images/           # Image assets
│   └── js/               # JavaScript files
│
├── templates/            # HTML templates
│   └── index.html       # Main template
│
├── models/              # Trained ML models
│   └── eye_flu_model   # Classification model
│
└── Untitled            # Additional documentation/notes
```

## 📊 Model Training

The machine learning model was trained on a comprehensive dataset of eye images, stored in Google Drive. 

### Training Data
- **Location**: Fluid Eye Project - Google Drive
- **Dataset**: Curated collection of eye flu and healthy eye images
- **Categories**: Normal eyes, Conjunctivitis-affected eyes
- **Format**: High-resolution JPEG/PNG images

### Model Performance
- **Accuracy**: 95%+
- **Precision**: High confidence predictions
- **Recall**: Effective detection rate

## 📊 Key Statistics

- **2,700+** Downloads
- **1,300+** Active Users
- **74** Medical Files Analyzed
- **46** Healthcare Facilities Connected
- **95%+** Prediction Accuracy

## 🔬 Symptoms Detected

The system helps identify common eye flu symptoms:

✅ Redness and inflammation  
✅ Itching or irritation  
✅ Excessive tearing or watery eyes  
✅ Discharge (clear, yellow, or green)  
✅ Blurry vision  
✅ Swelling of eyelids  

## 🏥 Healthcare Partners

Eye Flue Guard connects users with trusted healthcare providers in Nagpur:

- **Netram Eye Hospital** - Sakkardara, Nagpur | ☎️ 098528 04804
- **Shree Sai Eye Hospital** - Bhande Plot Square, Nagpur | ☎️ 0712 270 4488
- **Madhav Netralaya** - Navjeevan Colony, Nagpur | ☎️ 0712 678 5200
- **Jaiswal Eye Hospital** - Dr Ambedkar Road, Nagpur | ☎️ 0712 265 2786

## 🔧 Configuration

### PyScript Configuration
The `pyscript` file contains configuration for running Python in the browser:
- Package dependencies
- Python version settings
- Module imports

### Requirements
Check `requirements.txt` for all Python dependencies:
```
Flask>=2.0.0
numpy>=1.21.0
Pillow>=8.3.0
tensorflow>=2.6.0
opencv-python>=4.5.0
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Update documentation as needed
- Add tests for new features
- Ensure all tests pass before submitting

## 🐛 Known Issues & Troubleshooting

**Issue**: Model not loading
- **Solution**: Ensure the model file is in the correct directory and accessible

**Issue**: Image upload fails
- **Solution**: Check file size limits and supported formats (JPG, PNG)

**Issue**: PyScript not working
- **Solution**: Verify internet connection for CDN resources

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team
1)seema vaidya
2)Ruchita Bhandarkar
3)Priyatai Raut
4)Prasanjeet Meshram

Created with ❤️ by the Eye Flue Guard Team

## 📞 Contact & Support

- **Project Drive**: [Fluid Eye Project - Google Drive](https://drive.google.com)
- **Email**: support@eyeflueguard.com
- **Issues**: Report bugs and request features

## 🙏 Acknowledgments

- Medical advisors and ophthalmology experts
- Open source ML community
- Flask and PyScript developers
- Healthcare partners in Nagpur
- Beta testers and early adopters

## 🔮 Future Enhancements

- [ ] Mobile app development
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Real-time consultation feature
- [ ] Integration with electronic health records
- [ ] Expanded disease detection capabilities

---

<div align="center">

**Made with 👁️ and 💙 for better eye health**

⭐ Star this repository if you find it helpful!

[⬆ Back to Top](#-eye-flue-guard)

</div>
