from datetime import datetime


def get_date_range():
  from_date = input("Enter the 'From' date (mm/dd/yyyy): ")
  to_date = input("Enter the 'To' date (mm/dd/yyyy): ")
  return from_date, to_date


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


def create_employee_record(from_date, to_date, name, hours, rate, tax_rate):
  gross_pay, income_tax, net_pay = calculate_pay(hours, rate, tax_rate)
  return [
      from_date, to_date, name, hours, rate, gross_pay, tax_rate, income_tax,
      net_pay
  ]


def calculate_totals(records):
  totals = {
      "total_employees": len(records),
      "total_hours": sum(record[3] for record in records),
      "total_gross_pay": sum(record[5] for record in records),
      "total_tax": sum(record[7] for record in records),
      "total_net_pay": sum(record[8] for record in records)
  }
  return totals


def display_employee_info(record):
  print("\nEmployee Information")
  print("From Date: ", record[0])
  print("To Date: ", record[1])
  print("Employee Name: ", record[2])
  print("Total Hours: ", record[3])
  print("Hourly Rate: ", record[4])
  print("Gross Pay: ", record[5])
  print("Income Tax Rate: ", record[6])
  print("Income Tax: ", record[7])
  print("Net Pay: ", record[8])


def display_summary(totals):
  print("\nSummary")
  print("Total Employees: ", totals["total_employees"])
  print("Total Hours: ", totals["total_hours"])
  print("Total Gross Pay: ", totals["total_gross_pay"])
  print("Total Tax: ", totals["total_tax"])
  print("Total Net Pay: ", totals["total_net_pay"])


def main():
  records = []

  while True:
    from_date, to_date = get_date_range()
    name = get_employee_name()
    if name.lower() == "end":
      break

    hours = get_total_hours()
    rate = get_hourly_rate()
    tax_rate = get_tax_rate()

    record = create_employee_record(from_date, to_date, name, hours, rate,
                                    tax_rate)
    records.append(record)
    display_employee_info(record)

  totals = calculate_totals(records)
  display_summary(totals)


if __name__ == "__main__":
  main()
