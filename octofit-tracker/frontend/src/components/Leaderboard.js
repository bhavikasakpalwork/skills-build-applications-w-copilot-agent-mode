
const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const endpoint = codespace
      ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
      : 'http://localhost:8000/api/leaderboard/';
    console.log('Fetching Leaderboard from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setLeaderboard(results);
        console.log('Fetched Leaderboard:', results);
      })
      .catch(err => console.error('Error fetching leaderboard:', err));
  }, []);

  return (
    <div className="card mb-4">
      <div className="card-body">
        <h2 className="card-title mb-4">Leaderboard</h2>
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-dark">
              <tr>
                <th>#</th>
                {leaderboard[0] && Object.keys(leaderboard[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {leaderboard.map((entry, idx) => (
                <tr key={entry.id || idx}>
                  <td>{idx + 1}</td>
                  {leaderboard[0] && Object.keys(leaderboard[0]).map((key) => (
                    <td key={key}>{String(entry[key])}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Leaderboard;
