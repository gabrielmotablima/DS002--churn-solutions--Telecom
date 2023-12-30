import pandas as pd
from dataclasses import dataclass
from pandas.api.types import is_number

@dataclass
class CustomersDataPrep:

    binary_features = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "PaperlessBilling",
        "Churn"
    ]

    conditional_features = [
        "MultipleLines",    
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies"
    ]

    drop_columns = ["customerID"]

    comma_string_numbers = ["MonthlyCharges", "TotalCharges"]

    def __comma_to_number(
            self,
            series: pd.Series,
            typing: type=float
        ) -> pd.Series:
        return series.fillna("0").str.replace(",", ".").astype(typing)

    def __comma_numeric_string(
            self,
            df: pd.DataFrame
        ) -> pd.DataFrame:
        for feature in self.comma_string_numbers:
            df[feature] =      self.__comma_to_number(df[feature]) \
                          if   df[feature].dtype == "object" \
                          else df[feature]
        return df

    def __binarize_features(
            self,
            df: pd.DataFrame,
            conditionals:bool=False
        ) -> pd.DataFrame:
        if conditionals:
            for feature in self.conditional_features:
                if not is_number(df[feature][0]):
                    df[feature] = df[feature].mask(df[feature] != "Yes", "No").map({"Yes": 1, "No": 0})

        for feature in self.binary_features:
            if not is_number(df[feature][0]):
                df[feature] =      df[feature].map({"Yes": 1, "No": 0}) \
                              if   feature != "gender" \
                              else df[feature].map({"Male": 1, "Female": 0})    
        return df

    def prepare_data(
            self,
            df: pd.DataFrame,
            conditionals: bool = False
        ) -> pd.DataFrame:
        df = df.drop(columns=self.drop_columns, errors="ignore") \
            .pipe(self.__comma_numeric_string) \
            .pipe(self.__binarize_features, conditionals)
        return df