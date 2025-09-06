# 🎯 Placement Prediction System

A modern web application that predicts student placement chances based on CGPA and IQ scores using machine learning.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- 🎨 **Modern UI**: Beautiful, responsive web interface
- 🤖 **ML Prediction**: Real-time placement prediction using Random Forest
- 📊 **Input Validation**: Smart validation for CGPA (0.0-10.0) and IQ (50-200)
- 🚀 **Fast Performance**: Optimized Flask backend
- 📱 **Mobile Friendly**: Responsive design for all devices
- ⚡ **Real-time Results**: Instant prediction feedback

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Processing**: NumPy, Pandas
- **Styling**: Modern CSS with gradients and animations

## 📁 Project Structure

```text
placement_prediction/
├── api/
│   └── index.py          # Vercel serverless function
├── frontend/
│   └── index.html        # Main UI template
├── app.py                # Main Flask application
├── model.pkl             # Trained ML model
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── wsgi.py              # WSGI entry point
└── README.md            # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/vaibhav-1707/plactment_prediction.git
   cd plactment_prediction
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://127.0.0.1:5000` or `http://localhost:5000`

### 🚀 Vercel Deployment

1. **Connect your GitHub repository to Vercel**
2. **Deploy automatically** - Vercel will detect the configuration
3. **Your app will be live** at your Vercel URL

The application is pre-configured for Vercel with:

- `api/index.py` - Serverless function handler
- `vercel.json` - Deployment configuration
- Automatic dependency installation

## 🎮 How to Use

1. **Enter CGPA**: Input your CGPA score (0.0 - 10.0)
2. **Enter IQ Score**: Input your IQ score (50 - 200)
3. **Click Predict**: Get instant placement prediction
4. **View Results**: See if you'll be placed or not

## 📊 Model Information

- **Algorithm**: Random Forest Classifier
- **Features**: CGPA and IQ Score
- **Training Data**: 100+ student records
- **Accuracy**: Optimized for placement prediction
- **Prediction Logic**: Based on CGPA > 7.0 OR IQ > 120

## 🔧 API Endpoints

- `GET /` - Main application interface
- `POST /` - Submit prediction form
- `GET /<filename>` - Serve static files

## 📈 Sample Predictions

| CGPA | IQ Score | Prediction |
|------|----------|------------|
| 8.5  | 130      | ✅ Will be placed |
| 6.8  | 110      | ❌ Will not be placed |
| 7.2  | 125      | ✅ Will be placed |
| 6.5  | 95       | ❌ Will not be placed |

## 🛡️ Error Handling

- Input validation for CGPA and IQ ranges
- Graceful handling of missing model files
- User-friendly error messages
- Form validation on frontend

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds and smooth animations
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Elements**: Hover effects and smooth transitions
- **Color-coded Results**: Green for success, red for failure
- **Professional Typography**: Clean, readable fonts

## 🔮 Future Enhancements

- [ ] Add more features (projects, internships, etc.)
- [ ] Implement user authentication
- [ ] Add prediction confidence scores
- [ ] Create admin dashboard
- [ ] Add data visualization charts
- [ ] Implement model retraining pipeline

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

### Vaibhav Gautam

- GitHub: [@vaibhav-1707](https://github.com/vaibhav-1707)
- LinkedIn: [Vaibhav Gautam](https://linkedin.com/in/vaibhav-gautam)

## 🙏 Acknowledgments

- Scikit-learn team for the amazing ML library
- Flask team for the lightweight web framework
- Contributors and testers

## 📞 Support

If you have any questions or need help, feel free to:

- Open an issue on GitHub
- Contact me directly
- Check the documentation

---

⭐ **Star this repository if you found it helpful!**
