from carford.ext.database import db

def create_one(model_instance):
    try:
        db.session.add(model_instance)

        db.session.commit()
        return model_instance
    except:
        return False

def read_by_id(model_class, id):
    try:
        result = model_class.query.get(id)
        return result
    except:
        return False

def read_filter(model_class, model_class_prop, value):
    try:
        result = model_class.query.filter(model_class_prop == value)
        return result
    except:
        return False

def read_all(model_class):
    try:
        result = model_class.query.all()
        return result
    except:
        return False

def update(model_class, model_instance):
    try:
        read_instance = read_by_id(model_class, model_instance.id).to_dict()
        model_instance_dict = model_instance.to_dict()
        for key in read_instance:
            read_instance[key] = model_instance_dict[key]
        db.session.commit()
        return read_instance
    except:
        return False

def delete(model_class, id):
    try:
        query_filtered = model_class.query.filter_by(id = id)
        query_filtered.delete()
        db.session.commit()
        return id
    except:
        False

