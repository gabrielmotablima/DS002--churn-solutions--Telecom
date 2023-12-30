import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

@dataclass
class CustomersFeatureEng:

    internet_services = [
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    def __sum_internet_services(self, df: pd.DataFrame) -> pd.DataFrame:
        df["InternetServices"] = df[self.internet_services].sum(axis=1)
        return df

    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.pipe(self.__sum_internet_services)
        return df

    def __numeric_transformer(self) -> Pipeline:
        return Pipeline(steps=[
            ('scaler', StandardScaler())
        ])

    def __categorical_transformer(self) -> Pipeline:
        return Pipeline(steps=[
            ('encoder', OneHotEncoder())
        ])

    def preprocessor(
        self,
        numerical_features: list[str],
        categorical_features: list[str]
        ) -> ColumnTransformer:

        numeric_transformer = self.__numeric_transformer()
        categorical_transformer = self.__categorical_transformer()

        return ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)
            ])