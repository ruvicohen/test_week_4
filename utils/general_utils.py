from sqlalchemy import inspect


def to_dict(obj):
    if obj is None:
        return None
    obj_dict = {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}
    return obj_dict

def to_dict_with_relationships(obj):
    if obj is None:
        return None

    obj_dict = {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    for relationship in inspect(obj).mapper.relationships:
        related_value = getattr(obj, relationship.key)
        if relationship.uselist:  # If it's a list of related objects
            obj_dict[relationship.key] = [to_dict_with_relationships(related_obj) for related_obj in related_value]
        else:  # Single related object
            obj_dict[relationship.key] = to_dict_with_relationships(related_value)

    return obj_dict