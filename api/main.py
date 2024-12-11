from fastapi import FastAPI
from prediction import predict_price


app = FastAPI()

@app.get("/api/predict")
def predict(size,total_sqft,bath,balcony,location):
    price =  list(predict_price(size,total_sqft,bath,balcony,location))[0]
    return {"message":"success","Data":{"prediction_price":price},"Errorcode":0}
