TRUNCATE monthly_salary;INSERT INTO leave_requests (
    Req_id,
    Leave_SDate,
    Leave_EDate,
    Leave_Type,
    Applications,
    Statuses,
    Date_of_application,
    Dep_id,
    Emp_id
  )
VALUES (
    Req_id:int,
    'Leave_SDate:date',
    'Leave_EDate:date',
    'Leave_Type:varchar',
    'Applications:varchar',
    Statuses:int,
    'Date_of_application:date',
    'Dep_id:bigint',
    'Emp_id:bigint'
  );