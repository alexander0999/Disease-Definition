
concussion = ('РВОТА', 'ГОЛОВОКРУЖЕНИЕ', 'УЧАЩЕНИЕ ДЫХАНИЯ', 'ЧУВСТВИТЕЛЬНОСТЬ К СВЕТУ', 'ГОЛОВНАЯ БОЛЬ')
meningitis = ('ГОЛОВНАЯ БОЛЬ', 'ЧУВСТВИТЕЛЬНОСТЬ К СВЕТУ', 'СЛАБОСТЬ', 'ПОВЫШЕННАЯ ТЕМПЕРАТУРА', 'ТОШНОТА', 'РВОТА')
flu = ('ГОЛОВНАЯ БОЛЬ', 'ЖАР', 'ОЗНОБ', 'КАШЕЛЬ', 'БОЛЬ В ГОРЛЕ', 'БОЛЬ В СУСТАВАХ', 'НАСМОРК', 'ПЕРШЕНИЕ В ГОРЛЕ')

symptoms_list = input('Введите симптомы через запятую: ').upper().split(', ')


# search for the number of matches of the entered symptoms with the list of symptoms
def search_dis(symptoms, list):
    matched_symptom = 0
    for i in range(len(symptoms)):
         if symptoms[i] in list:
           matched_symptom += 1
    return matched_symptom


# search for matches in the list of symptoms to identify diseases
dis_concussion = search_dis(symptoms_list, concussion)
dis_meningitis = search_dis(symptoms_list, meningitis)
dis_flu = search_dis(symptoms_list, flu)


# search for the maximum number of matches to determine the disease
def result(dis_concussion, dis_meningitis, dis_flu):
    max_value = max(dis_concussion, dis_meningitis, dis_flu)
    if max_value == dis_concussion and max_value == dis_meningitis and max_value == dis_flu:
      return 1
    if max_value == dis_concussion:
      return 2
    if max_value == dis_meningitis:
      return 3
    if max_value == dis_flu:
      return 4


value_guess_result = result(dis_concussion, dis_meningitis, dis_flu)


# conclusion of the alleged disease
def end(value_guess_result):
    if value_guess_result == 1:
      return print('Проверьте правильность ввода данных или напишите больше симптомов')
    if value_guess_result == 2:
      coincidence_of_symptoms = round(((dis_concussion / len(concussion)) * 100), 0)
      return print(f'Скорее всего, это - сотрясение мозга. (Совпадение симптомов: {int(coincidence_of_symptoms)}%)')
    if value_guess_result == 3:
      coincidence_of_symptoms = round(((dis_meningitis / len(meningitis)) * 100), 0)
      return print(f'Скорее всего, это - менингит. (Совпадение симптомов: {int(coincidence_of_symptoms)}%)')
    if value_guess_result == 4:
      coincidence_of_symptoms = round(((dis_flu / len(flu)) * 100), 0)
      return print(f'Скорее всего, это - грипп. (Совпадение симптомов: {int(coincidence_of_symptoms)}%)')


end(value_guess_result)
