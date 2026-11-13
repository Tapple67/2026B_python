import joblib
import pandas as pd

class BikeService:
    # learning.py 테스트 결과 (모델 재학습 시 갱신)
    MAE = 163.88   # 평균적으로 몇 대 틀리는지
    RMSE = 255.87

    def __init__(self, model_path: str = "bike_model.pkl"):
        self.model = joblib.load(model_path)

    def predict_rental_count(self, data: dict) -> float:
        df = pd.DataFrame([{
            "Hour": data["Hour"],
            "Temperature": data["Temperature"],
            "Humidity(%)": data["Humidity"],
            "Wind speed (m/s)": data["Wind_speed"],
            "Visibility (10m)": data["Visibility"],
            "Dew point temperature": data["Dew_point_temperature"],
            "Solar Radiation (MJ/m2)": data["Solar_Radiation"],
            "Rainfall(mm)": data["Rainfall"],
            "Snowfall (cm)": data["Snowfall"],
            "Seasons": data["Seasons"],
            "Holiday": data["Holiday"],
            "dayofweek": data["dayofweek"],
        }])

        pred = float(self.model.predict(df)[0])
        return round(max(0.0, pred), 1)

bike_service = BikeService()