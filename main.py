from Model.DataModelDto import DataModelDto
from fastapi import FastAPI
from functions.PreparaArray import PreparaArray
from functions.PercorreArray import PercorreArray

app = FastAPI()

@app.post("/data/")
def collectData(data: DataModelDto):
    valores = PreparaArray.transformaString(data.data)
    factor = PercorreArray.verificaFatorDoArray(valores)
    message = PercorreArray.confirmaSeEntrouFatorNovo(factor)
    return {"message": message, "factor": factor, "data": data.data}