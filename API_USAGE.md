# How to Use the Deployed Mtcars Prediction API

### Base URL

```
https://mtcars-api-481459706523.us-central1.run.app/predict
```

### Endpoint

```
POST /predict
```

### Required Headers

```
Content-Type: application/json
```

### Sample JSON Input

```json
{
  "cyl": 6,
  "disp": 160,
  "hp": 110,
  "drat": 3.9,
  "wt": 2.62,
  "qsec": 16.46,
  "vs": 0,
  "am": 1,
  "gear": 4,
  "carb": 4
}
```

### Sample Response

```json
{
  "mpg": 21.0
}
```

### Example with Curl

```bash
curl -X POST https://mtcars-api-481459706523.us-central1.run.app/predict   -H "Content-Type: application/json"   -d '{"cyl":6,"disp":160,"hp":110,"drat":3.9,"wt":2.62,"qsec":16.46,"vs":0,"am":1,"gear":4,"carb":4}'
```
