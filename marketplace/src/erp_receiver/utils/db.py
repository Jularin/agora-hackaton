import json

from django.db import IntegrityError

from erp_receiver.models import models_dict, Product, Category, MeasureUnit


def save_category(data: dict) -> None:
    parent = Category.objects.filter(id=data["parent"]).first()
    data["parent"] = parent
    try:
        Category.objects.create(**data)
    except IntegrityError:
        pass


def save_measure_unit(data: dict) -> None:
    try:
        MeasureUnit.objects.create(**data)
    except IntegrityError:
        pass


def save_product(data: dict) -> None:
    category = Category.objects.filter(id=data["category"]).first()
    measure_unit = MeasureUnit.objects.filter(id=data["measure_unit"]).first()
    product_type = Product.types_dict[data["product_type"]]

    data["category"] = category
    data["measure_unit"] = measure_unit
    data["product_type"] = product_type
    try:
        product = Product.objects.create(**data)
        print(product)
    except IntegrityError:
        pass


dict_with_save_functions = {"category": save_category, "measure_unit": save_measure_unit, "product": save_product}


def save_upload_data_from_dict(data: dict) -> None:
    for model_key in data.keys():
        for model_kwargs in data[model_key]:
            if model_kwargs.get("delete"):
                model_object = models_dict[model_key].objects.get(model_kwargs["id"])
                model_object.delete()

            model_kwargs.pop("delete")

            dict_with_save_functions[model_key](model_kwargs)


def save_upload_data_from_str(data:str) -> None:
    data = json.loads(data)

    save_upload_data_from_dict(data)
