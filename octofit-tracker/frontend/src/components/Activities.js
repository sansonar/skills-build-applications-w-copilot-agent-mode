import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    const fetchActivities = async () => {
      const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        console.log('Fetched Activities:', data);
        setActivities(data.results || data); // Handle paginated or plain array responses
      } catch (error) {
        console.error('Error fetching activities:', error);
      }
    };

    fetchActivities();
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map((activity, index) => (
          <li key={index}>{activity.name || `Activity ${index + 1}`}</li>
        ))}
      </ul>
    </div>
  );
};

export default Activities;