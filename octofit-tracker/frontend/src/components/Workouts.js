import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        console.log('Fetched Workouts:', data);
        setWorkouts(data.results || data); // Handle paginated or plain array responses
      } catch (error) {
        console.error('Error fetching workouts:', error);
      }
    };

    fetchWorkouts();
  }, []);

  return (
    <div>
      <h1>Workouts</h1>
      <ul>
        {workouts.map((workout, index) => (
          <li key={index}>{workout.name || `Workout ${index + 1}`}</li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;