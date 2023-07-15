factorList = []
class PercorreArray:


    def confirmaSeEntrouFatorNovo(factor):
        if factor < 2:
            return 'Sem alteração nos padrões'    
        if factor in factorList:
            return 'Sem alteração nos padrões'
        else:
            factorList.append(factor)
            factorList.sort()
            print(factorList)
            return 'Novo Padrão encontrado'


    def verificaFatorDoArray(valores):
        valores.sort()
        temp = 0
        index = 0
        factor = 0
        condition = True
        for val in valores:
            if index == 1:
                factor = val / temp
            elif index > 1:
                factorTemp = val / temp
                if(factorTemp != factor):
                    condition == False
            index += 1
            temp = val
            if(condition == False):
                break
        if(condition == True):
            return factor
        else:
            return -1

            



