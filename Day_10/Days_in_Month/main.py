def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year")
        return True
      else:
        # print("Not leap year")
        return False
    else:
    #   print("Leap year")
      return True
  else:
    # print("Not leap year")
    return False
  
# print(is_leap(2018))

# TODO: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if is_leap(year) == False:
      if month == 2:
          return 28
      elif month == 4 or month == 6 or month == 9 or month == 11:
          return 30
      else:
          return 31
  else:
      if month == 2:
          return 29
      elif month == 4 or month == 6 or month == 9 or month == 11:
          return 30
      else:
          return 31

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

