bmw_models = {"M5": {"engine": "4.4L Turbocharged V8", "power": "441 kW", "torque": "750 Nm"},
              "i3": {"engine": "Electric Motor", "power": "125 kW", "torque": "250 Nm"}}

def add_model(model, engine, power, torque):
    bmw_models[model] = {"engine": engine, "power": power, "torque": torque}

add_model("X7", "3.0L Turbocharged 6-cylinder", "294 kW", "650 Nm")
add_model("X5", "3.0L Turbocharged 6-cylinder", "195 kW", "620 Nm")
add_model("M8", "4.4L Turbocharged V8", "460 kW", "750 Nm")
add_model("M2", "3.0L Turbocharged 6-cylinder", "272 kW", "465 Nm")
add_model("M3", "3.0L Turbocharged 6-cylinder", "331 kW", "550 Nm")
add_model("M4", "3.0L Turbocharged 6-cylinder", "317 kW", "550 Nm")
add_model("M6", "4.4L Turbocharged V8", "441 kW", "750 Nm")
add_model("M7", ".L Turbocharged -cylinder", " kW", " Nm")
add_model("320I", "2.0L Turbocharged 4-cylinder", "135 kW", "290 Nm")
add_model("330I", "2.0L Turbocharged 4-cylinder", "185 kW", "350 Nm")
add_model("340I", "3.0L Turbocharged 6-cylinder", "240 kW", "450 Nm")
add_model("318D", "2.0L Turbocharged 4-cylinder", "110 kW", "320 Nm")
add_model("320D", "2.0L Turbocharged 4-cylinder", "140 kW", "400 Nm")
add_model("330D", "3.0L Turbocharged 6-cylinder", "195 kW", "620 Nm")
add_model("535I", "3.0L Turbocharged 6-cylinder", "225 kW", "400 Nm")
add_model("525I", "2.5L Turbocharged 6-cylinder", "141 kW", "250 Nm")
add_model("528I", "2.8L Turbocharged 6-cylinder", "170 kW", "280 Nm")
add_model("530I", "3.0L Turbocharged 6-cylinder", "193 kW", "300 Nm")
add_model("550D", "4.4L Turbocharged V8", "284 kW", "740 Nm")
add_model("550I", "4.4L Turbocharged V8", "300 kW", "600 Nm")
add_model("X1", "2.0L Turbocharged 4-cylinder", "140 kW", "400 Nm")
add_model("X2", "2.0L Turbocharged 4-cylinder", "140 kW", "400 Nm")
add_model("X3", "3.0L Turbocharged 6-cylinder", "195 kW", "620 Nm")
add_model("X4", "3.0L Turbocharged 6-cylinder", "245 kW", "450 Nm")
add_model("520D", "2.0L Turbocharged 4-cylinder", "135 kW", "380 Nm")
add_model("525D", "2.5L Turbocharged 6-cylinder", "150 kW", "400 Nm")
add_model("530D", "3.0L Turbocharged 6-cylinder", "170 kW", "520 Nm")
add_model("730D", "2.9L Turbocharged 6-cylinder", "195 kW", "620 Nm")
add_model("740I", "3.0L Turbocharged 6-cylinder", "250 kW", "450 Nm")
add_model("750I", "4.4L Turbocharged V8", "330 kW", "650 Nm")
add_model("760I", "6.0L Turbocharged V12", "448 kW", "850 Nm")

model = input("Enter BMW model: ")
if model in bmw_models:
    print("Engine: ", bmw_models[model]["engine"])
    print("Power: ", bmw_models[model]["power"])
    print("Torque: ", bmw_models[model]["torque"])
else:
    print("Model not found.")
"""
bmw_models = {
    "e46 330i": {"Horsepower": 225, "Torque": 214, "Engine": "M54B30", "Cylinders": 6},
    "e39 540i": {"Horsepower": 282, "Torque": 324, "Engine": "M62B44", "Cylinders": 8},
    "e60 550i": {"Horsepower": 360, "Torque": 360, "Engine": "N62B48", "Cylinders": 8},
    "e90 335i": {"Horsepower": 300, "Torque": 300, "Engine": "N54B30", "Cylinders": 6},
    "f10 550i": {"Horsepower": 400, "Torque": 450, "Engine": "N63B44", "Cylinders": 8},
}

def bmw_info(model):
    if model in bmw_models:
        return bmw_models[model]
    else:
        return "Invalid BMW model. Please try again."

model = input("Enter a BMW model (e.g. e46 330i): ")
print(bmw_info(model))
"""