import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, mean_squared_log_error

# 1) Carica i dati
df_train = pd.read_csv(r'C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 22 06-05\kaggle_competition\data\train.csv')
df_test  = pd.read_csv(r'C:\Users\fabri\Desktop\MarcoPatierno_DepositoCorsoPython\env\Giorno 22 06-05\kaggle_competition\data\test.csv')

# 2) Feature engineering
def make_features(df):
    df = df.copy()
    df['Sex'] = df['Sex'].map({'male':0,'female':1})
    df['BMI']  = df['Weight'] / (df['Height']/100)**2
    df['BSA']  = 0.007184 * df['Weight']**0.425 * df['Height']**0.725
    df['Delta_Temp']       = df['Body_Temp'] - 37.0
    df['HR_per_kg']        = df['Heart_Rate'] / df['Weight']
    df['Heart_Beats_Total']= df['Heart_Rate'] * df['Duration']
    df['log_Duration']     = np.log1p(df['Duration'])
    df['sqrt_Duration']    = np.sqrt(df['Duration'])
    df['BMR'] = np.where(
        df['Sex']==0,
        88.362 + 13.397*df['Weight'] + 4.799*df['Height'] - 5.677*df['Age'],
        447.593 +  9.247*df['Weight'] + 3.098*df['Height'] - 4.330*df['Age']
    )
    df['MaxHR']   = 220 - df['Age']
    df['pct_MaxHR']= df['Heart_Rate'] / df['MaxHR']
    df['HR_Dur2'] = df['Heart_Rate'] * (df['Duration']**2)
    return df

train_fe = make_features(df_train)
test_fe  = make_features(df_test)

X_raw      = train_fe.drop(columns=['id','Calories'])
y_orig     = train_fe['Calories']
X_test_raw = test_fe.drop(columns=['id'])

# 3) Log‐trasformazione di tutte le feature
X      = X_raw.copy()
X_test = X_test_raw.copy()
for col in X.columns:
    m = min(X[col].min(), X_test[col].min())
    shift = -m+1 if m<=0 else 0
    X[col]      = np.log1p(X[col] + shift)
    X_test[col] = np.log1p(X_test[col] + shift)

# 4) Split e target in log per ottimizzare RMSLE
X_train, X_val, y_train_o, y_val_o = train_test_split(
    X, y_orig, test_size=0.2, random_state=42
)
y_train = np.log1p(y_train_o)
y_val   = np.log1p(y_val_o)

# 5) Iperparametri da esplorare
param_dist = {
    'learning_rate':    [0.01, 0.05, 0.1],
    'max_depth':        [5, 7, 10, 12],
    'min_child_weight': [1, 5, 10],
    'gamma':            [0, 0.1, 0.2, 0.5],
    'subsample':        [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'reg_alpha':        [0, 0.01, 0.1, 1],
    'reg_lambda':       [1, 2, 5],
    'booster':          ['gbtree', 'dart']
}

# 6) XGBRegressor con eval_metric e early_stopping_rounds in constructor
xgb = XGBRegressor(
    objective='reg:squarederror',
    n_estimators=1000,
    eval_metric='rmse',
    early_stopping_rounds=50,
    random_state=42,
    verbosity=0
)

# 7) RandomizedSearchCV (si passa solo eval_set e verbose a fit)
search = RandomizedSearchCV(
    xgb,
    param_distributions=param_dist,
    n_iter=50,
    scoring='neg_mean_squared_log_error',
    cv=5,
    verbose=1,
    n_jobs=-1,
    random_state=42
)

search.fit(
    X_train, y_train,
    eval_set=[(X_val, y_val)],
    verbose=False
)

best = search.best_estimator_

# 8) Metriche CV e validation
cv_rmsle  = np.sqrt(-search.best_score_)
y_val_pred = np.expm1(best.predict(X_val))
val_rmse   = np.sqrt(mean_squared_error(y_val_o, y_val_pred))
val_rmsle  = np.sqrt(mean_squared_log_error(y_val_o, y_val_pred))

print("Best params:", search.best_params_)
print(f"CV RMSLE: {cv_rmsle:.4f}")
print(f"Validation RMSE: {val_rmse:.4f}, RMSLE: {val_rmsle:.4f}")

# 9) Predizioni finali sul test set
df_test['Pred_Calories'] = np.expm1(best.predict(X_test))
print(df_test[['id','Pred_Calories']].head())
