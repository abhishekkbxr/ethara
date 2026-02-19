import { useEffect, useMemo, useState } from 'react';

const INITIAL_FORM = {
  employee: '',
  date: '',
  status: 'Present',
};

export default function AttendanceForm({ employees, selectedEmployeeId, onSubmit, loading }) {
  const [form, setForm] = useState({
    ...INITIAL_FORM,
    employee: selectedEmployeeId ? String(selectedEmployeeId) : '',
  });

  useEffect(() => {
    if (!selectedEmployeeId) return;
    setForm((prev) => ({ ...prev, employee: String(selectedEmployeeId) }));
  }, [selectedEmployeeId]);

  const isComplete = useMemo(() => form.employee && form.date && form.status, [form]);

  function handleChange(event) {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    try {
      await onSubmit({
        employee: Number(form.employee),
        date: form.date,
        status: form.status,
      });
      setForm((prev) => ({ ...prev, date: '', status: 'Present' }));
    } catch {
      // Keep entered values when submission fails.
    }
  }

  return (
    <form className="inline-form" onSubmit={handleSubmit}>
      <label>
        Employee
        <select
          name="employee"
          value={form.employee}
          onChange={handleChange}
          required
          disabled={loading || employees.length === 0}
        >
          <option value="">Select employee</option>
          {employees.map((employee) => (
            <option key={employee.id} value={employee.id}>
              {employee.employee_id} - {employee.full_name}
            </option>
          ))}
        </select>
      </label>
      <label>
        Date
        <input type="date" name="date" value={form.date} onChange={handleChange} required />
      </label>
      <label>
        Status
        <select name="status" value={form.status} onChange={handleChange} required>
          <option value="Present">Present</option>
          <option value="Absent">Absent</option>
        </select>
      </label>
      <button className="button button--primary" type="submit" disabled={!isComplete || loading}>
        {loading ? 'Saving...' : 'Mark Attendance'}
      </button>
    </form>
  );
}
