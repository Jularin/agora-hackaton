from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict

import xmltodict


class ParserInterface(ABC):
    @abstractmethod
    def parse(self, data) -> dict:
        pass


class Context:
    def __init__(self, strategy: ParserInterface) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> ParserInterface:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ParserInterface) -> None:
        self._strategy = strategy

    def parse(self, raw_data):
        result = self._strategy.parse(raw_data)

        return result


class XMLParser(ParserInterface):
    def parse(self, data) -> Dict:
        result = {}
        data = xmltodict.parse(data)["AgoraMessage"]
        categories = data.get("ГруппаНоменклатура")
        if categories:
            result["category"] = [
                {
                    "id": category["Ссылка"],
                    "parent": category.get("Родитель"),
                    "name": category["Наименование"],
                    "delete": bool(int(category["ПометкаУдаления"]))
                }
                for category in categories
            ]

        measure_units = data.get("ЕдиницыИзмерения")
        if measure_units:
            # in case if only one measure unit
            if isinstance(measure_units, dict):
                measure_units = measure_units["Строка"]
                result["measure_unit"] = [
                    {
                        "id": measure_units.get("Ссылка"),
                        "name": measure_units["Наименование"],
                        "full_name": measure_units["НаименованиеПолное"],
                        "delete": measure_units.get("ПометкаУдаления")
                    }
                ]
            else:
                result["measure_unit"] = [
                    {
                        "id": measure_unit["Строка"].get("Ссылка"),
                        "name": measure_unit["Строка"]["Наименование"],
                        "full_name": measure_unit["Строка"]["НаименованиеПолное"],
                        "delete": measure_unit["Строка"].get("ПометкаУдаления")
                    }
                    for measure_unit in measure_units
                ]

        items = data.get("Номенклатура")
        if items:
            # in case if only one item
            if isinstance(items, dict):
                result["product"] = [
                    {
                        "id": items["Ссылка"],
                        "category": items["Родитель"],
                        "code": items["Артикул"],
                        "name": items["Наименование"],
                        "description": items["Описание"],
                        "product_type": items["ТипНоменклатуры"],
                        "rate_nds": float(items["СтавкаНДС"][:-1]),
                        "measure_unit": items["ЕдиницаХраненияОстатков"],
                        "delete": bool(int(items["ПометкаУдаления"]))
                    }
                ]
            else:
                result["product"] = [
                    {
                        "id": item["Ссылка"],
                        "category": item["Родитель"],
                        "code": item["Артикул"],
                        "name": item["Наименование"],
                        "description": item["Описание"],
                        "product_type": item["ТипНоменклатуры"],
                        "rate_nds": float(item["СтавкаНДС"][:-1]),
                        "measure_unit": item["ЕдиницаХраненияОстатков"],
                        "delete": bool(int(item["ПометкаУдаления"]))
                    }
                    for item in items
                ]

        return result
