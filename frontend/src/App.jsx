import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/applied-jobs")
      .then((res) => {
        setJobs(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <div className="app">
      <h1>JobForge AI Dashboard</h1>

      {jobs.length === 0 ? (
        <p>No jobs applied yet</p>
      ) : (
        jobs.map((job, index) => (
          <div className="card" key={index}>
            <h2>{job.title}</h2>
            <p>Company: {job.company}</p>
            <p>ATS Score: {job.score}%</p>
            <p>Status: {job.status}</p>
          </div>
        ))
      )}
    </div>
  );
}

export default App;