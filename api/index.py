import json

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"
    
    # Load the list of student objects
    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)  # data is a list of dicts

    # Get 'name' query parameters (can be multiple)
    names = request.query.getlist("name")
    
    # Build a mapping from name to marks
    name_to_marks = {item["name"]: item["marks"] for item in data}
    
    # Find marks for each requested name (in order)
    marks = [name_to_marks.get(name, None) for name in names]
    
    return response.json({"marks": marks})
