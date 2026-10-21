from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    title="Seismic AI Interpretation API",
    version="0.1.0",
    description="Прототип API для дипломного проекта по автоматизированной интерпретации сейсморазведочных данных.",
)

@app.get("/")
def root():
    return {
        "project": "Seismic AI Interpretation",
        "status": "prototype"
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # TODO: добавить проверку формата файла
    # TODO: preprocessing
    # TODO: заменить mock на реальную ML-модель
    return {
        "filename": file.filename,
        "status": "accepted",
        "model": "mock",
        "message": "Файл принят. ML-модель будет подключена на следующем этапе."
    }
