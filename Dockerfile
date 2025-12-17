FROM 

WORKDIR /app

COPY requirements.txt .

RUN npm install

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
