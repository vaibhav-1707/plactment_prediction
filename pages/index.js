import { useState } from 'react';
import Head from 'next/head';

export default function Home() {
  const [cgpa, setCgpa] = useState('');
  const [iq, setIq] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          cgpa: parseFloat(cgpa),
          iq: parseInt(iq),
        }),
      });

      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      setPrediction({ error: 'Failed to get prediction' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Head>
        <title>Placement Prediction</title>
        <meta name="description" content="Predict your placement chances based on CGPA and IQ" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="container">
        <div className="card">
          <h1>🎯 Placement Prediction</h1>
          <p className="subtitle">Enter your CGPA and IQ score to predict your placement chances</p>
          
          <form onSubmit={handleSubmit} className="form">
            <div className="form-group">
              <label htmlFor="cgpa">CGPA (0-10)</label>
              <input
                type="number"
                id="cgpa"
                value={cgpa}
                onChange={(e) => setCgpa(e.target.value)}
                min="0"
                max="10"
                step="0.1"
                required
                placeholder="Enter your CGPA"
              />
            </div>

            <div className="form-group">
              <label htmlFor="iq">IQ Score</label>
              <input
                type="number"
                id="iq"
                value={iq}
                onChange={(e) => setIq(e.target.value)}
                min="50"
                max="200"
                required
                placeholder="Enter your IQ score"
              />
            </div>

            <button type="submit" disabled={loading} className="submit-btn">
              {loading ? '🔮 Predicting...' : '🔮 Predict Placement'}
            </button>
          </form>

          {prediction && (
            <div className={`prediction ${prediction.error ? 'error' : prediction.placed ? 'success' : 'warning'}`}>
              {prediction.error ? (
                <span>❌ {prediction.error}</span>
              ) : (
                <span>{prediction.placed ? '✅' : '❌'} {prediction.prediction}</span>
              )}
            </div>
          )}
        </div>
      </div>

      <style jsx>{`
        .container {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          padding: 20px;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }

        .card {
          background: white;
          border-radius: 20px;
          padding: 40px;
          box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
          max-width: 500px;
          width: 100%;
          text-align: center;
        }

        h1 {
          color: #333;
          margin-bottom: 10px;
          font-size: 2.5rem;
          font-weight: 700;
        }

        .subtitle {
          color: #666;
          margin-bottom: 30px;
          font-size: 1.1rem;
        }

        .form {
          display: flex;
          flex-direction: column;
          gap: 20px;
        }

        .form-group {
          text-align: left;
        }

        label {
          display: block;
          margin-bottom: 8px;
          font-weight: 600;
          color: #333;
          font-size: 1rem;
        }

        input {
          width: 100%;
          padding: 15px;
          border: 2px solid #e1e5e9;
          border-radius: 10px;
          font-size: 1rem;
          transition: border-color 0.3s ease;
          box-sizing: border-box;
        }

        input:focus {
          outline: none;
          border-color: #667eea;
        }

        .submit-btn {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          border: none;
          padding: 15px 30px;
          border-radius: 10px;
          font-size: 1.1rem;
          font-weight: 600;
          cursor: pointer;
          transition: transform 0.2s ease;
          margin-top: 10px;
        }

        .submit-btn:hover:not(:disabled) {
          transform: translateY(-2px);
        }

        .submit-btn:disabled {
          opacity: 0.7;
          cursor: not-allowed;
        }

        .prediction {
          margin-top: 25px;
          padding: 20px;
          border-radius: 10px;
          font-size: 1.2rem;
          font-weight: 600;
          animation: slideIn 0.3s ease;
        }

        .prediction.success {
          background: #d4edda;
          color: #155724;
          border: 2px solid #c3e6cb;
        }

        .prediction.warning {
          background: #fff3cd;
          color: #856404;
          border: 2px solid #ffeaa7;
        }

        .prediction.error {
          background: #f8d7da;
          color: #721c24;
          border: 2px solid #f5c6cb;
        }

        @keyframes slideIn {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @media (max-width: 600px) {
          .card {
            padding: 30px 20px;
            margin: 10px;
          }

          h1 {
            font-size: 2rem;
          }

          .container {
            padding: 10px;
          }
        }
      `}</style>
    </>
  );
}
