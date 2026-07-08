import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# read in csv
df = pd.read_csv("./code/data/CAdata.csv", encoding='latin1', on_bad_lines='skip', lineterminator='\n', quotechar='"')
print(df.head())  # Print the first few rows to verify that the data has been loaded correctly


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/dates/{date}/")
def read_item_withdate(date: str, q: str | None = None):
    # get item from df
    item = df[(df['trending_date'] == date) & (q is None or df['title'] == q)]
    print(item)
    filtered_item = item.to_dict(orient='records')
    filtered_item = [i for i in filtered_item if i['trending_date'] == date and (q is None or i['title'] == q)]
    display_item = filtered_item[0] if filtered_item else None
    display_item = {k: v for k, v in display_item.items() if k in ['video_id', 'title', 'trending_date']}
    return {"date": date, "item": display_item}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: str | None = None):
    # get item from df
    item = df[df['video_id'] == item_id]
    print(item)
    filtered_item = item.to_dict(orient='records')
    display_item = filtered_item[0] if filtered_item else None
    display_item = {k: v for k, v in display_item.items() if k in ['video_id', 'title', 'trending_date']}
    return {"item_id": item_id, "q": q, "item": display_item}

