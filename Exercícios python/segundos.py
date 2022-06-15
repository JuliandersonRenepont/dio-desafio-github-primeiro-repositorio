segundos = input("Por favor, entre com o número de segundos que deseja converter:")
total_segundos = int(segundos)

horas = total_segundos // 3600
dias = horas//86400

segundos_restantes = total_segundos % 3600
minutos = segundos_restantes // 60
segundos_restantes_final = segundos_restantes % 60

if (horas >= 24):
    dias = int(horas / 24)
    horas = int(horas % 24)

print(dias,"dias,",horas,"horas,",minutos,"minutos","e",segundos_restantes_final,"segundos.")  
