from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
#ashritha is bad bondam#
#chitti chikamma is bad girl#


app = Flask(__name__)

#app.config['SECRET_KEY'] = "JLKJJJO3IURYoiouolnojojouuoo=5y9y9youjuy952oohhbafdnoglhoho"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenseDB.db'

db = SQLAlchemy(app)



# Step 1: Define a model
class ExampleModel(db.Model):
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
    model_instance = ExampleModel()
    # Set the attributes of the model instance based on the JSON data
    model_instance.attribute1 = item['attribute1']
    model_instance.attribute2 = item['attribute2']
    # Set more attributes here as needed

    db.session.add(model_instance)
    db.session.commit()


# Step 3: Parse and insert JSON data
""" json_data = '[{"name": "John", "age": 25}, {"name": "Alice", "age": 30}]'
data_array = json.loads(json_data)

for data in data_array:
    name = data['name']
    age = data['age']
    model_instance = ExampleModel(name, age)
    db.session.add(model_instance)

db.session.commit() """
