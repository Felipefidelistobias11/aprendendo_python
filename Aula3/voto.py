idade = int(input("Qual é a sua idade?"))

if idade < 16 :
    print("Você não pode votar")
elif idade < 18 :
    print("Você pode escolher se quer votar")
elif idade > 65 :
    print("Você pode escolher se quer votar")
else :
    print("Você é obrigado a votar")