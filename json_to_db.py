""" from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application import routes
import json


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = True)
    

#app.config['SECRET_KEY'] = "JLKJJJO3IURYoiouolnojojouuoo=5y9y9youjuy952oohhbafdnoglhoho"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'

db = SQLAlchemy(app)




# Step 1: Define a model
class DashboardData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    end_year = db.Column(db.Integer)
    intensity = db.Column(db.Integer)
    sector = db.Column(db.String(50))
    topic = db.Column(db.String(50))
    insight = db.Column(db.String(50))
    url = db.Column(db.String(150))
    region = db.Column(db.String(50))
    start_year = db.Column(db.String(50))
    impact = db.Column(db.String(50))
    added = db.Column(db.String(50))
    published = db.Column(db.String(50))
    country = db.Column(db.String(50))
    relevance = db.Column(db.Integer)
    pestle = db.Column(db.String(50))
    source = db.Column(db.String(50))
    title = db.Column(db.String(100))
    likelihood = db.Column(db.Integer)   
    

def __init__(self, end_year, intensity, sector, topic, insight, url, region, start_year, impact, added, published, country, relevance, pestle, source, title, likelihood):       
            self.end_year = end_year
            self.intensity = intensity
            self.sector = sector
            self.topic = topic
            self.insight = insight
            self.url = url
            self.region = region
            self.start_year = start_year
            self.impact = impact
            self.added = added
            self.published = published
            self.country = country
            self.relevance = relevance
            self.pestle = pestle
            self.source = source
            self.title = title
            self.likelihood = likelihood

# Step 2: Create a database table

app.app_context().push()
db.create_all()

with open('jsondata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    #lines = data.readlines()
    #print(data)

for item in data:
    model_instance = DashboardData()
    # Set the attributes of the model instance based on the JSON data
    model_instance.end_year = item['end_year']
    model_instance.intensity = item['intensity']
    model_instance.sector = item['sector']
    model_instance.topic = item['topic']
    model_instance.insight = item['insight']
    model_instance.url = item['url']
    model_instance.region = item['region']
    model_instance.start_year = item['start_year']
    model_instance.impact = item['impact']
    model_instance.added = item['added']
    model_instance.published = item['published']
    model_instance.country = item['country']
    model_instance.relevance = item['relevance']
    model_instance.pestle = item['pestle']
    model_instance.source = item['source']
    model_instance.title = item['title']
    model_instance.likelihood = item['likelihood']
    # Set more attributes here as needed

    db.session.add(model_instance)
    db.session.commit()

   # print(data)
# Step 3: Parse and insert JSON data
""" json_data = '[{"name": "John", "age": 25}, {"name": "Alice", "age": 30}]'
data_array = json.loads(json_data)

for data in data_array:
    name = data['name']
    age = data['age']
    model_instance = ExampleModel(name, age)
    db.session.add(model_instance)

db.session.commit() """
 """