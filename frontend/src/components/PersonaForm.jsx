
import React, { useState } from "react";

function PersonaForm() {
  const [form, setForm] = useState({
    first_name: "",
    last_name: "",
    jobTitle: "",
    company: "",
    location: "",
    industry: "",
    experience: "",
    profile_url: "",
    email: "",
    phone: ""
  });

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const API_URL = import.meta.env.VITE_BACKEND_URL;

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
  setLoading(true);
  setMessage("");

  try {
    const res = await fetch(`${API_URL}/prospects`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...form,
        experience: Number(form.experience)
      })
    });

    if (!res.ok) {
      const err = await res.text();
      throw new Error(err);
    }

    setMessage("✅ Data successfully stored in Google Sheets");
  } catch (err) {
    console.error(err);
    setMessage("❌ Backend error. Check logs.");
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="form-wrapper">
      <div className="form-scroll">
        <div className="form-grid">
          {[
            ["first_name", "First Name"],
            ["last_name", "Last Name"],
            ["jobTitle", "Job Title"],
            ["company", "Company"],
            ["location", "Location"],
            ["industry", "Industry"],
            ["experience", "Experience (years)"],
            ["profile_url", "Profile URL"],
            ["email", "Email"],
            ["phone", "Phone"]
          ].map(([name, label]) => (
            <div className="field" key={name}>
              <label>{label}</label>
              <input
                name={name}
                value={form[name]}
                onChange={handleChange}
                placeholder={label}
              />
            </div>
          ))}
        </div>
      </div>

      <div className="form-footer">
        <button onClick={handleSubmit} disabled={loading}>
          {loading ? "Exporting..." : "Export to Google Sheets"}
        </button>
        {message && <p className="status">{message}</p>}
      </div>
    </div>
  );
}

export default PersonaForm;
