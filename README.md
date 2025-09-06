# 🎯 Placement Prediction App

A modern web application that predicts whether a student will be placed based on their CGPA and IQ score. Built with Next.js and deployed on Vercel.

## 🚀 Features

- **Modern React UI**: Beautiful, responsive interface built with Next.js
- **Real-time Predictions**: Instant prediction results with smooth animations
- **API Integration**: RESTful API for programmatic access
- **Mobile Responsive**: Perfect experience on all devices
- **Fast Performance**: Optimized for speed and user experience
- **Zero Configuration**: Deploys instantly on Vercel

## 🛠️ Technology Stack

- **Frontend**: Next.js 14, React 18
- **Styling**: Styled JSX (CSS-in-JS)
- **API**: Next.js API Routes
- **Deployment**: Vercel (Serverless)
- **Language**: JavaScript/TypeScript

## 📁 Project Structure

```text
placement_prediction/
├── pages/
│   ├── index.js          # Main application page
│   └── api/
│       └── predict.js    # Prediction API endpoint
├── package.json          # Dependencies and scripts
├── next.config.js        # Next.js configuration
├── model.pkl             # Trained ML model (for reference)
└── README.md            # Project documentation
```

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/vaibhav-1707/plactment_prediction.git
   cd plactment_prediction
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   ```
   http://localhost:3000
   ```

### Vercel Deployment

1. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will automatically detect Next.js

2. **Deploy**
   - Click "Deploy" in the Vercel dashboard
   - Your app will be live at `https://your-app.vercel.app`

## 📊 How It Works

### Input Parameters
- **CGPA**: Cumulative Grade Point Average (0-10 scale)
- **IQ Score**: Intelligence Quotient score

### Prediction Logic
The application uses a rule-based prediction system:
- **High Performance**: CGPA ≥ 8.0 + IQ ≥ 120 → ✅ Will be placed
- **Good Performance**: CGPA ≥ 7.0 + IQ ≥ 110 → ✅ Will be placed
- **Average Performance**: CGPA ≥ 6.5 + IQ ≥ 100 → ✅ Will be placed
- **Below Average**: Otherwise → ❌ Will not be placed

### Output
- **✅ Will be placed**: High probability of getting placed
- **❌ Will not be placed**: Low probability of getting placed

## 🔧 API Usage

### Predict Placement
```bash
POST /api/predict
Content-Type: application/json

{
  "cgpa": 8.5,
  "iq": 130
}
```

**Response:**
```json
{
  "prediction": "Will be placed",
  "placed": true,
  "cgpa": 8.5,
  "iq": 130
}
```

## 🎨 Features

### User Interface
- **Modern Design**: Clean, gradient-based interface
- **Form Validation**: Real-time input validation
- **Loading States**: Smooth loading animations
- **Responsive Layout**: Perfect on desktop and mobile
- **Error Handling**: User-friendly error messages
- **Smooth Animations**: CSS transitions and keyframes

### Technical Features
- **Serverless Architecture**: Deployed on Vercel
- **Fast Performance**: Optimized Next.js build
- **SEO Optimized**: Meta tags and proper structure
- **Type Safety**: TypeScript support ready
- **Hot Reload**: Instant development feedback

## 🚀 Deployment

### Vercel (Recommended)
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Deploy automatically with zero configuration

### Other Platforms
- **Netlify**: Compatible with Next.js
- **Railway**: Deploy with Docker
- **DigitalOcean**: App Platform support

## 📈 Performance

- **Fast Loading**: Optimized Next.js build
- **Low Latency**: Serverless functions
- **High Availability**: 99.9% uptime with Vercel
- **Global CDN**: Fast access worldwide
- **Image Optimization**: Next.js automatic optimization

## 🔒 Security

- **Input Validation**: All inputs are validated
- **Error Handling**: Secure error messages
- **HTTPS**: Encrypted connections
- **No Data Storage**: No personal data is stored
- **XSS Protection**: Built-in Next.js security

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

### Vaibhav Gautam
- **GitHub**: [@vaibhav-1707](https://github.com/vaibhav-1707)
- **LinkedIn**: [Vaibhav Gautam](https://linkedin.com/in/vaibhav-gautam)
- **Email**: vaibhav.gautam@example.com

## 🙏 Acknowledgments

- Thanks to the Next.js team for the amazing framework
- Vercel for the seamless deployment platform
- The React community for continuous innovation

---

**⭐ If you found this project helpful, please give it a star!**