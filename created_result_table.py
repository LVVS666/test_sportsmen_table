import json

from datetime import datetime as dt

sport = {}
sport_result = []

result_run_list = ''
with open("results_RUN.txt", "r") as f:
    for i in f:
       result_run_list += i

result_run_list = result_run_list.split()
result_run_list[0]= '287'

with open('competitors2.json', 'r', encoding='utf-8') as f:
    sportmans_numbers_result = json.load(f)
    for key, value in sportmans_numbers_result.items():
        for key_in_num in result_run_list:
            if key == key_in_num:
                sport[key]= [
                    value['Surname'],
                    value['Name'],
                    {result_run_list[result_run_list.index(key_in_num)+1]:
                     result_run_list[result_run_list.index(key_in_num)+2]
                     },
                    {result_run_list[result_run_list.index(key_in_num)+4]:
                     result_run_list[result_run_list.index(key_in_num)+5]
                     }
                    ]

for _, creat_result in sport.items():
    time_finish = creat_result[3]['finish']
    time_start = creat_result[2]['start']
    time_1 = dt.strptime(time_finish, '%H:%M:%S,%f')
    time_2 = dt.strptime(time_start, '%H:%M:%S,%f')
    time_result = time_1 - time_2
    creat_result.append({'result': str(time_result)})


for i, j in sport.items():
    sport_result.append([i, j[0], j[1], j[4]['result']])

sport_total = sorted(sport_result, key=lambda x: x[3])
number_sportsman = 0

print(f'''
| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |
| --- | --- | --- | --- | --- |'''
     )
for output_result in sport_total:
    number_sportsman += 1
    print(f'| {number_sportsman} | {output_result[0]} | {output_result[1]} | {output_result[2]} | {output_result[3][2:]} |')