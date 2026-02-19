export default function AttendanceTable({ records }) {
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Employee</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.date}</td>
              <td>
                {record.employee_code} - {record.employee_name}
              </td>
              <td>
                <span
                  className={
                    record.status === 'Present' ? 'status status--present' : 'status status--absent'
                  }
                >
                  {record.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
