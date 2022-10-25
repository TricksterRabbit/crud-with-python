def model_list_to_json(model_object):
    mapped_model_object = map(lambda item: item.to_json(), model_object)
    return list(mapped_model_object)
