from flask import Blueprint

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
def getdata():
    return { 'some': 'value'}


#Create Car Endpoint
@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    specs = request.json['specs']
    mileage = request.json['mileage']
    max_speed = request.json['max_speed']
    dimensions = request.json['dimensions']
    weight = request.json['weight']
    cost_of_prod = request.json['cost_of_prod']
    series = request.json['series']
    make = request.json['make']

    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    car = Car(name,description,price, specs,mileage,max_speed,dimensions, weight,cost_of_prod,series, make, user_token = user_token )

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(cars)
    return jsonify(response)




# RETRIEVE ALL Cars ENDPOINT
@api.route('/cars', methods = ['GET'])
@token_required
def get_car(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = car_schema.dump(cars)
    return jsonify(response)


# RETRIEVE ONE Car ENDPOINT
@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        cars = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401



# UPDATE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['POST','PUT'])
@token_required
def update_car(current_user_token,id):
    car = Car.query.get(id) # GET CAR INSTANCE

    car.name = request.json['name']
    car.description = request.json['description']
    car.price = request.json['price']
    car.specs = request.json['specs']
    car.mileage = request.json['mileage']
    car.max_speed = request.json['max_speed']
    car.dimensions = request.json['dimensions']
    car.weight = request.json['weight']
    car.cost_of_prod = request.json['cost_of_prod']
    car.series = request.json['series']
    car.make = request.json['make']
    car.user_token = current_user_token.token

    db.session.commit()
    response = car.dump(car)
    return jsonify(response)


# DELETE CAR ENDPOINT
@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    response = car.dump(car)
    return jsonify(response)