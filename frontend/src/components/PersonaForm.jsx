const React = require("react")
const axios = require("axios")

module.exports = function PersonaForm() {
  const [form, setForm] = React.useState({})

  const submit = async () => {
    await axios.post("http://localhost:8000/prospects", form)
    alert("Exported to Google Sheets")
  }

  return (
    <div>
      <input placeholder="Job Title" onChange={e => setForm({...form, jobTitle: e.target.value})} />
      <input placeholder="Years of Experience" onChange={e => setForm({...form, experience: Number(e.target.value)})} />
      <input placeholder="Location" onChange={e => setForm({...form, location: e.target.value})} />
      <input placeholder="Industry" onChange={e => setForm({...form, industry: e.target.value})} />
      <button onClick={submit}>Export to Google Sheets</button>
    </div>
  )
}
