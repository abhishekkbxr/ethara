function StatCard({ label, value }) {
  return (
    <article className="stat-card">
      <span>{label}</span>
      <strong>{value}</strong>
    </article>
  );
}

export default function DashboardStats({ summary, totalEmployees }) {
  return (
    <section className="stat-grid">
      <StatCard label="Employees" value={totalEmployees} />
      <StatCard label="Attendance Records" value={summary.total_records || 0} />
      <StatCard label="Present Entries" value={summary.total_present || 0} />
      <StatCard label="Absent Entries" value={summary.total_absent || 0} />
    </section>
  );
}
