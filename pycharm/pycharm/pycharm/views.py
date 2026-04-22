from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = pd.read_csv(r"D:\collage project\machine learning\diabetes.csv")

    x = data.drop('Outcome', axis=1)
    y = data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LogisticRegression(max_iter=200)  # أحيانًا تحتاج زيادة max_iter
    model.fit(x_train, y_train)

    val1 = float(request.GET.get('n1'))
    val2 = float(request.GET.get('n2'))
    val3 = float(request.GET.get('n3'))
    val4 = float(request.GET.get('n4'))
    val5 = float(request.GET.get('n5'))
    val6 = float(request.GET.get('n6'))
    val7 = float(request.GET.get('n7'))
    val8 = float(request.GET.get('n8'))


    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])

    result2 = "Positive" if pred[0] == 1 else "Negative"

    return render(request, 'predict.html', {"result2": result2})
