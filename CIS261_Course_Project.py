
def get_employee_name():
  return input("Enter employee name: ")


def get_total_hours():
  return float(input("Enter total hours: "))


def get_hourly_rate():
  return float(input("Enter hourly rate: "))


def get_tax_rate():
  return float(input("Enter income tax rate: "))


def calculate_pay(hours, rate, tax_rate):
  gross_pay = hours * rate
  income_tax = gross_pay * (tax_rate / 100)
  net_pay = gross_pay - income_tax
  return gross_pay, income_tax, net_pay


def display_employee_info(name, hours, rate, gross_pay, tax_rate, income_tax,
                          net_pay):
  print("Employee Name: ", name)
  print("Total Hours: ", hours)
  print("Hourly Rate: ", rate)
  print("Gross Pay: ", gross_pay)
  print("Income Tax Rate: ", tax_rate)
  print("Income Tax: ", income_tax)
  print("Net Pay: ", net_pay)


def display_summary(total_employees, total_hours, total_gross_pay, total_tax,
                    total_net_pay):
  print("Total Employees: ", total_employees)
  print("Total Hours: ", total_hours)
  print("Total Gross Pay: ", total_gross_pay)
  print("Total Tax: ", total_tax)
  print("Total Net Pay: ", total_net_pay)


def main():
  # Initialize variables
  total_employees = 0
  total_hours = 0
  total_gross_pay = 0
  total_tax = 0
  total_net_pay = 0

  while True:
    # Get employee details
    name = get_employee_name()
    if name.lower() == "end":
      break

    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    # Calculate pay
    gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)

    # Update totals
    total_employees += 1
    total_hours += hours
    total_gross_pay += gross_pay
    total_tax += income_tax
    total_net_pay += net_pay

    # Display employee info
    display_employee_info(name, hours, rate, gross_pay, tax_rate, income_tax,
                          net_pay)

  # Display summary
  display_summary(total_employees, total_hours, total_gross_pay, total_tax,
                  total_net_pay)


if __name__ == "__main__":
  main()
