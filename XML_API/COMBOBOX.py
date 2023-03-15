import re
from typing import Dict
from ITEM import Item

class ComboBox:
    def __init__(self, combobox: Dict):
        self.name = combobox.get('name', False)
        self.label = combobox.get('label', False)
        self.active = combobox.get('active', False)
        self.visible = combobox.get('visible', False)
        self.default = combobox.get('default', False)
        self.valuetype = combobox.get('valuetype', False)
        self.nosave = combobox.get('nosave', False)
        self.locked = combobox.get('locked', False)
        self.geo_influencing = combobox.get('geo_influencing', False)
        self.combo_items = []

    @staticmethod
    def _check_element_exists(element: str, _list: Dict) -> bool:
        ''' Check if an element exists in a dictionary '''
        return element in _list

    def _get_xml_string(self) -> str:
        ''' Generate XML string for ComboBox object '''
        _local_attrs = []

        if self.name:
            _local_attrs.append(f'name="{self.name}"')

        if self.label:
            _local_attrs.append(f'label="{self.label}"')

        if self.active:
            _local_attrs.append(f'active="{self.active}"')

        if self.visible:
            _local_attrs.append(f'visible="{self.visible}"')

        if self.default:
            _local_attrs.append(f'default="{self.default}"')

        if self.valuetype:
            _local_attrs.append(f'valuetype="{self.valuetype}"')

        if self.nosave:
            _local_attrs.append(f'nosave="{self.nosave}"')

        if self.locked:
            _local_attrs.append(f'locked="{self.locked}"')

        if self.geo_influencing:
            _local_attrs.append(f'geoInfluencing="{self.geo_influencing}"')

        _xml_out = f"<COMBOBOX {' '.join(_local_attrs)}>"

        if not self.combo_items:
            _xml_out += "</COMBOBOX>"
        else:
            for item in self.combo_items:
                _xml_out += '\n' + item.return_item_element()
            _xml_out += "\n</COMBOBOX>"

        _xml_out = re.sub(' +', ' ', _xml_out)
        return _xml_out

    def print_as_xml_item(self) -> None:
        ''' Print ComboBox as XML string '''
        print(self._get_xml_string())

    def add_item(self, data: Dict) -> None:
        ''' Add item to ComboBox '''
        _local_item = Item(data)
        self.combo_items.append(_local_item)

combo = ComboBox({'name': 'asd', 'label': 'aasd', 'geo_influencing': 'True'})

combo.add_item({'value':'test', 'label':'Text label'})
combo.add_item({'value':'test1', 'label':'Text label'})
combo.add_item({'value':'test2', 'label':'Text label'})
combo.print_as_xml_item()
