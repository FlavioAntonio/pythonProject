from datetime import datetime
from pytz import timezone
# data_str_data = '20/04/2024'
# data_format = "%d/%m/%Y"
# data = datetime.strptime(data_str_data, data_format)
# print("Data convertida: ", data)

# data = datetime.now()
# print(data.timestamp())
# print(datetime.fromtimestamp(1767316943.412563))

fmt = '%d/%m/%Y'

data = datetime.strptime('2022/12/13 15:30:00', '%Y/%m/%d %H:%M:%S')
print(data.strftime(fmt))