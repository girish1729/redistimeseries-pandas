import redis
import json # To make the responses easier to read

# Data from two sensors
sensor1 = {
    "sensorId": 1,
    "areaId": 20,
    "data": [
        { "timestamp": 1652824475581, "temperature": 23.9, "humidity":
29  },
        { "timestamp": 1652828015127, "temperature": 22.8, "humidity":
27  },
        { "timestamp": 1652831657886, "temperature": 21.7, "humidity":
28  },
        { "timestamp": 1652835287321, "temperature": 19.4, "humidity":
35  },
        { "timestamp": 1652838756149, "temperature": 17.8, "humidity":
40  }
    ]
}

sensor2 = {
    "sensorId": 2,
    "areaId": 24,
    "data": [
        { "timestamp": 1652824475581, "temperature": 18.3, "humidity":
51  },
        { "timestamp": 1652828015127, "temperature": 17.2, "humidity":
54  },
        { "timestamp": 1652831657886, "temperature": 16.7, "humidity":
56  },
        { "timestamp": 1652835287321, "temperature": 15.6, "humidity":
60  },
        { "timestamp": 1652838756149, "temperature": 14.4, "humidity":
65  }
    ]
}

sensors = [ sensor1, sensor2 ]

# Connect to a Redis database
r = redis.Redis()

# Create a list to store keys
key_list = []
# Create a list of keys and values for ts.madd
humidity_madd_list = []
# For each sensor:
for sensor in sensors:
    # Create time series keys
    key_end = "{}:{}".format(sensor["sensorId"], sensor["areaId"])
    temperature_key = "temperature-py:" + key_end
    humidity_key = "humidity-py:" + key_end
    key_list.extend((temperature_key, humidity_key))

    print("Create {} and {}".format(temperature_key, humidity_key))

    labels = { "sensorId" : sensor["sensorId"], "areaId" :
sensor["areaId"] }
    labels["dataType"] = "temperature"
    r.ts().create(temperature_key, labels=labels)

    labels["dataType"] = "humidity"
    r.ts().create(humidity_key, labels=labels)


    # Add temperature data to time series keys with ts.add
    print("Add data to {}".format(temperature_key))
    # For each data entry:
    for entry in sensor["data"]:
        r.ts().add(temperature_key, entry["timestamp"],
entry["temperature"])
        #Create a list of humidity data for ts.madd
        humidity_madd_list.append( (humidity_key, entry["timestamp"],
entry["humidity"]))

#Add humidity data to time series keys with ts.madd
print("Add data with ts.madd:\n{}".format(humidity_madd_list))
r.ts().madd(humidity_madd_list)
input("\nAdded all data. Press enter to continue...")

print("Get the last value from temperature-py:1:20...")
get_reply = r.ts().get("temperature-py:1:20")
print(json.dumps(get_reply, indent=4) + "\n")

print("Get all of the values from humidity-py:2:24...")
range_reply = r.ts().range("humidity-py:2:24", 0, "+")
print(json.dumps(range_reply, indent=4) + "\n")

print("Get last values from area 20...")
mget_filters = ["areaId=20"]
mget_reply = r.ts().mget(mget_filters, with_labels=True)
print(json.dumps(mget_reply, indent=4) + "\n")

print("Get all of the values from sensor 2 from earliest to latest...")
mrange_filters = [ "sensorId=2" ]
mrange_reply = r.ts().mrange(0, "+", mrange_filters, with_labels=True)
print(json.dumps(mrange_reply, indent=4) + "\n")

print("Get all humidity values from latest to earliest...")
mrevrange_filters = [ "dataType=humidity" ]
mrevrange_reply = r.ts().mrevrange(0, "+", mrevrange_filters,
with_labels=True)
print(json.dumps(mrevrange_reply, indent=4) + "\n")

print("Delete range of values from temperature-py:1:20...")
r.ts().delete("temperature-py:1:20", 0, 1652831657886)
range_reply = r.ts().range("temperature-py:1:20", 0, "+")
print(json.dumps(range_reply, indent=4) + "\n")

input("Press enter to finish...")
print("Deleting keys: {}".format(key_list))
for key in key_list:
    r.delete(key)
print("Done!")

