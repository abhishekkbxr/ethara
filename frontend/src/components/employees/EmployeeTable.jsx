export default function EmployeeTable({ employees, selectedEmployeeId, onSelectEmployee, onDelete, deleting }) {
  return (
    <div className="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Employee ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Department</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((employee) => {
            const isSelected = employee.id === selectedEmployeeId;
            return (
              <tr key={employee.id} className={isSelected ? 'is-selected' : ''}>
                <td>{employee.employee_id}</td>
                <td>{employee.full_name}</td>
                <td>{employee.email}</td>
                <td>{employee.department}</td>
                <td>
                  <div className="table-actions">
                    <button
                      type="button"
                      className="button button--ghost"
                      onClick={() => onSelectEmployee(employee.id)}
                    >
                      {isSelected ? 'Viewing' : 'View Attendance'}
                    </button>
                    <button
                      type="button"
                      className="button button--danger"
                      onClick={() => onDelete(employee.id)}
                      disabled={deleting === employee.id}
                    >
                      {deleting === employee.id ? 'Deleting...' : 'Delete'}
                    </button>
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
