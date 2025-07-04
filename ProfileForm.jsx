import React, { useState } from "react";
import axios from "axios";

export default function ProfileForm() {
  const [form, setForm] = useState({ name: "", skills: "", goals: "" });
  const [gigs, setGigs] = useState("");
  const [tip, setTip] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setGigs("");
    setTip("");

    try {
      const res = await axios.post("http://localhost:5000/api/profile/upload", form);
      setGigs(res.data.gigs || "No gigs returned");
      setTip(res.data.coachingTip || "No tip provided");
    } catch (err) {
      console.error("💥 Submission error:", err);
      setError("Failed to submit profile. Check backend server or API key.");
    }
  };

  return (
    <div style={{ padding: "1rem", maxWidth: "500px" }}>
      <h2>🧑‍💻 FlexMatch Profile</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="name"
          placeholder="Your Name"
          value={form.name}
          onChange={handleChange}
          required
        />
        <br /><br />
        <textarea
          name="skills"
          placeholder="Your Skills"
          value={form.skills}
          onChange={handleChange}
          required
        />
        <br /><br />
        <textarea
          name="goals"
          placeholder="Your Goals"
          value={form.goals}
          onChange={handleChange}
          required
        />
        <br /><br />
        <button type="submit">Submit</button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {gigs && (
        <div>
          <h3>💼 Matched Gigs:</h3>
          <pre>{gigs}</pre>
        </div>
      )}

      {tip && (
        <div>
          <h4>💡 Coaching Tip:</h4>
          <p>{tip}</p>
        </div>
      )}
    </div>
  );
}