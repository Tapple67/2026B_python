from fastapi import APIRouter
from pydantic import BaseModel
from Service import bike_service

router = APIRouter(tags=["Bike Prediction"])

class BikeInput(BaseModel):
    Hour: int
    Temperature: float
    Humidity: float
    Wind_speed: float
    Visibility: float
    Dew_point_temperature: float
    Solar_Radiation: float
    Rainfall: float
    Snowfall: float
    Seasons: str      # 'Spring', 'Summer', 'Autumn', 'Winter'
    Holiday: str      # 'Holiday', 'No Holiday'
    dayofweek: int    # 0(월) ~ 6(일)

@router.post("/predict")
def predict(data: BikeInput):
    result = bike_service.predict_rental_count(data.model_dump())
    mae = bike_service.MAE
    return {
        "predicted_count": result,
        "mae": mae,
        "rmse": bike_service.RMSE,
        "lower": round(max(0.0, result - mae), 1),  # 예측 범위 (± MAE)
        "upper": round(result + mae, 1),
    }