import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [data, setData] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME || window.location.hostname.replace('-8000.app.github.dev', '');
  const url = `https://${codespace}-8000.app.github.dev/api/leaderboard/`;

  useEffect(() => {
    console.log('Fetching Leaderboard from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = Array.isArray(json) ? json : json.results || [];
        setData(results);
        console.log('Leaderboard data:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, [url]);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-primary">
              <tr>
                {data[0] && Object.keys(data[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((item, idx) => (
                <tr key={item.id || idx}>
                  {data[0] && Object.keys(data[0]).map((key) => (
                    <td key={key}>{String(item[key])}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {data.length === 0 && <div className="alert alert-info">No leaderboard data found.</div>}
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
