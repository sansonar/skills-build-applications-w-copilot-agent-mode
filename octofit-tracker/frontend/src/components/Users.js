import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    const fetchUsers = async () => {
      const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        console.log('Fetched Users:', data);
        setUsers(data.results || data); // Handle paginated or plain array responses
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    };

    fetchUsers();
  }, []);

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user, index) => (
          <li key={index}>{user.name || `User ${index + 1}`}</li>
        ))}
      </ul>
    </div>
  );
};

export default Users;