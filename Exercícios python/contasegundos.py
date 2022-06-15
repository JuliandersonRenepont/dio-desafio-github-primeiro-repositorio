#Programa que converte os segundos em horas
#minutos e segundos finais.

segundos_ = input("Entre com os segundos que deseja converter: ")

segundos_total = int(segundos_)

horas = segundos_total // 3600

segundos_restantes = segundos_total % 3600

minutos = segundos_total // 60

seg_rest_final = segundos_total % 60



print(horas, "horas, ", minutos, "minutos e", seg_rest_final, "segundos")
