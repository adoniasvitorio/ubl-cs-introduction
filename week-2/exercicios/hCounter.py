seconds_str = input('Digite o numero de segundos que deseja converter: ')
total_seconds = int(seconds_str)

hour = total_seconds // 3600
rSeconds = total_seconds % 3600
minutes = rSeconds // 60
seconds = rSeconds % 60

print(hour, ' horas, ', minutes, 'minutos e', seconds, 'segundos')
