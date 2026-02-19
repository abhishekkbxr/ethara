const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL?.replace(/\/$/, '') || 'http://127.0.0.1:8000/api';

async function request(path, options = {}) {
  let response;
  try {
    response = await fetch(`${API_BASE_URL}${path}`, {
      headers: {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
      },
      ...options,
    });
  } catch {
    throw new Error('Could not connect to the backend API.');
  }

  const contentType = response.headers.get('content-type') || '';
  const data = contentType.includes('application/json') ? await response.json() : null;

  if (!response.ok) {
    const flattenedErrors =
      data?.errors && typeof data.errors === 'object'
        ? Object.values(data.errors)
            .flat()
            .map((value) => String(value))
            .join(' ')
        : '';
    const errorMessage =
      data?.error || flattenedErrors ||
      'Something went wrong. Please try again.';
    const error = new Error(errorMessage);
    error.status = response.status;
    error.details = data;
    throw error;
  }

  return data;
}

export function getEmployees() {
  return request('/employees/');
}

export function createEmployee(payload) {
  return request('/employees/', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function removeEmployee(employeePk) {
  return request(`/employees/${employeePk}/`, {
    method: 'DELETE',
  });
}

export function getAttendance({ employeeId, date }) {
  const params = new URLSearchParams();
  if (employeeId) params.set('employee_id', employeeId);
  if (date) params.set('date', date);
  const query = params.toString();
  return request(`/attendance/${query ? `?${query}` : ''}`);
}

export function getEmployeeAttendance(employeePk) {
  return request(`/employees/${employeePk}/attendance/`);
}

export function createAttendance(payload) {
  return request('/attendance/', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export function getDashboardSummary() {
  return request('/dashboard/');
}
