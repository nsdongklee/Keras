from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7]])     # (5,3)
y = array([4,5,6,7,8])     # (5, ) == [] 하나만 넣으면 1D array이다. 내가 생각했던 (1,5)는 2D array

# Data reshape
print(x.shape[0], x.shape[1])

x = x.reshape(x.shape[0], x.shape[1], 1)



#2. 모델 구성
model = Sequential()

model.add(LSTM(10, activation='relu', input_shape=(3,1))) # (열, 몇개씩 자를지)
model.add(Dense(5))
model.add(Dense(1))

model.summary()


#3. 훈련
model.compile(loss='mse', optimizer='adam', metrics=['mae'])
model.fit(x, y, epochs=100, batch_size=1)


#4. 평가예측
loss, mae = model.evaluate(x, y, batch_size=1)
print('mae: ', mae)

x_prd = array([6,7,8])
x_prd = x_prd.reshape(1,3,1)
p = model.predict(x_prd, batch_size=1)

print(p)
