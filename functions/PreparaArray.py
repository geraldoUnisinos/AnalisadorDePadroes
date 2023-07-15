from Model.DataModelDto import DataModelDto


class PreparaArray:
    def transformaString(data: str):
        valores = []
        for val in data.split(', '):
            valores.append(int(val))
        return valores