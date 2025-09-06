export default function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { cgpa, iq } = req.body;

    // Validate input
    if (typeof cgpa !== 'number' || typeof iq !== 'number') {
      return res.status(400).json({ error: 'CGPA and IQ must be numbers' });
    }

    if (cgpa < 0 || cgpa > 10) {
      return res.status(400).json({ error: 'CGPA must be between 0 and 10' });
    }

    if (iq < 50 || iq > 200) {
      return res.status(400).json({ error: 'IQ must be between 50 and 200' });
    }

    // Simple prediction logic
    function predictPlacement(cgpa, iq) {
      if (cgpa >= 8.0 && iq >= 120) {
        return 1; // Will be placed
      } else if (cgpa >= 7.0 && iq >= 110) {
        return 1; // Will be placed
      } else if (cgpa >= 6.5 && iq >= 100) {
        return 1; // Will be placed
      } else {
        return 0; // Will not be placed
      }
    }

    const result = predictPlacement(cgpa, iq);
    const prediction = result === 1 ? "Will be placed" : "Will not be placed";

    res.status(200).json({
      prediction,
      placed: Boolean(result),
      cgpa,
      iq
    });

  } catch (error) {
    res.status(500).json({ error: 'Internal server error' });
  }
}
