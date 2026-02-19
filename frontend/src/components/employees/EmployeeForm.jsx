import { useMemo, useState } from 'react';

const INITIAL_FORM = {
  employee_id: '',
  full_name: '',
  email: '',
  department: '',
};

export default function EmployeeForm({ onSubmit, loading }) {
  const [form, setForm] = useState(INITIAL_FORM);
  const isComplete = useMemo(
    () =>
      form.employee_id.trim() &&
      form.full_name.trim() &&
      form.email.trim() &&
      form.department.trim(),
    [form]
  );

  function handleChange(event) {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    try {
      await onSubmit({
        employee_id: form.employee_id.trim(),
        full_name: form.full_name.trim(),
        email: form.email.trim(),
        department: form.department.trim(),
      });
      setForm(INITIAL_FORM);
    } catch {
      // Keep entered values when submission fails.
    }
  }

  return (
    <form className="stack-form" onSubmit={handleSubmit}>
      <label>
        Employee ID
        <input
          type="text"
          name="employee_id"
          value={form.employee_id}
          onChange={handleChange}
          placeholder="EMP-001"
          required
        />
      </label>
      <label>
        Full Name
        <input
          type="text"
          name="full_name"
          value={form.full_name}
          onChange={handleChange}
          placeholder="Ava Johnson"
          required
        />
      </label>
      <label>
        Email Address
        <input
          type="email"
          name="email"
          value={form.email}
          onChange={handleChange}
          placeholder="ava@company.com"
          required
        />
      </label>
      <label>
        Department
        <input
          type="text"
          name="department"
          value={form.department}
          onChange={handleChange}
          placeholder="Engineering"
          required
        />
      </label>
      <button className="button button--primary" type="submit" disabled={!isComplete || loading}>
        {loading ? 'Saving...' : 'Add Employee'}
      </button>
    </form>
  );
}
