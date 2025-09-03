tabu = int(input("Digite um numero para gerar sua tabuada\n"))

while tabu != 0:
    for contador in range(11):
        print (f"{tabu} X {contador} = {tabu * contador}")
    tabu = int(input("Digite um numero para gerar sua tabuada\n"))
