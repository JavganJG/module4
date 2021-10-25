dictionary = {
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": True,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
    
  ],
  "children": [],
  "spouse": None
}
print(dictionary["phoneNumbers"][1]["number"])
dictionary["phoneNumbers"].append({
    "type": "private",
    "number": "999 999-9999"
})