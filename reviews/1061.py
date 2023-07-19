ULTIMA_POSICAO = -1
day_1 = int(input().split()[ULTIMA_POSICAO])
h1, m1, s1 = map(int,input().split(':'))

day_2 = int(input().split()[ULTIMA_POSICAO])
h2, m2, s2 = map(int,input().split(':'))

start_in_seconds = (day_1 * 24 * 60 * 60) + (h1 * 60 * 60)  + (m1 * 60) + s1
final_in_seconds = (day_2 * 24 * 60 * 60) + (h2 * 60 * 60 ) + (m2 * 60) + s2

delta_time = final_in_seconds - start_in_seconds

# 2 23:59:00 | 3 00:01:00
# 2 5 3

# print(time_in_sec_2 - time_in_sec_1)

SECONDS_IN_ONE_DAY = (24 * 60 * 60)
SECONDS_IN_ONE_HOUR = (60 * 60)
SECONDS_IN_ONE_MINUTE = (60)

delta_days = delta_time // SECONDS_IN_ONE_DAY
delta_time -= delta_days * SECONDS_IN_ONE_DAY

delta_hours = delta_time // SECONDS_IN_ONE_HOUR
delta_time -= delta_hours * SECONDS_IN_ONE_HOUR

delta_minutes = delta_time // SECONDS_IN_ONE_MINUTE
delta_time -= delta_minutes * SECONDS_IN_ONE_MINUTE

delta_seconds = delta_time

# for _ in range(time_in_sec_1, time_in_sec_2):
#     delta_seconds += 1
#     if  delta_seconds == 60:
#         delta_minutes += 1
#         s = 0
#     if delta_minutes == 60:
#            delta_hours += 1
#            delta_minutes = 0
#     if  delta_hours == 24:
#             delta_days += 1
#             delta_hours = 0

print(f"{delta_days} Dias",
      f"{delta_hours} horas",
      f"{delta_minutes} minutos",
      f"{delta_seconds} sedundos",
      sep = '\n')