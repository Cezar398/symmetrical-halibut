import re

class Item:
    def __init__(self, item):
        ''' Initialize ITEM ELEMENT '''
        self.value = item.get('value', False)
        self.label = item.get('label', False)
        self.info_list = item.get('info_list', False)
        self.image1 = item.get('image1', False)
        self.image2 = item.get('image2', False)

    def print_as_list(self):
        ''' PRINT ITEM AS LIST '''
        _templist = []
        if self.value is not False:
            _templist.append(self.value)

        if self.label is not False:
            _templist.append(self.label)

        if self.info_list is not False:
            _templist.append(self.info_list)

        if self.image1 is not False:
            _templist.append(self.image1)

        if self.image2 is not False:
            _templist.append(self.image2)

        print(_templist)

    def print_as_xml_item(self):
        ''' PRINT ITEM AS LIST '''
        if self.value is not False:
            _local_value = f'value="{self.value}" '

        if self.label is not False:
            _local_label = f'label="{self.label}" '

        _local_info_list = str()

        if self.info_list is not False:
            index = 1
            for item in self.info_list:
                _local_info_list = _local_info_list + f'info{index}="{item}" '
                index = index + 1

        if self.image1 is not False:
            _local_image1 = f'image1="{self.image1}" '

        if self.image2 is not False:
            _local_image2 = f'image2="{self.image2}" '

        _xml_out = "<ITEM "

        if self.value is not False:
            _xml_out += _local_value

        if self.label is not False:
            _xml_out += _local_label

        if self.info_list is not False:
            _xml_out += _local_info_list

        if self.image1 is not False:
            _xml_out += _local_image1

        if self.image2 is not False:
            _xml_out += _local_image2

        _xml_out += "/>"
        _xml_out = re.sub(' +', ' ', _xml_out)
        print(_xml_out)

    def return_item_element(self):
        ''' PRINT ITEM AS LIST '''
        if self.value is not False:
            _local_value = f'value="{self.value}" '

        if self.label is not False:
            _local_label = f'label="{self.label}" '

        _local_info_list = str()

        if self.info_list is not False:
            index = 1
            for item in self.info_list:
                _local_info_list = _local_info_list + f'info{index}="{item}" '
                index = index + 1

        if self.image1 is not False:
            _local_image1 = f'image1="{self.image1}" '

        if self.image2 is not False:
            _local_image2 = f'image2="{self.image2}" '

        _xml_out = "<ITEM "

        if self.value is not False:
            _xml_out += _local_value

        if self.label is not False:
            _xml_out += _local_label

        if self.info_list is not False:
            _xml_out += _local_info_list

        if self.image1 is not False:
            _xml_out += _local_image1

        if self.image2 is not False:
            _xml_out += _local_image2

        _xml_out += "/>"
        _xml_out = re.sub(' +', ' ', _xml_out)

        return _xml_out
