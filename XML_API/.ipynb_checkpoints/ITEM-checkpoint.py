import re

class ITEM:
    def __init__(self, item):
        ''' Init ITEM ELEMENT '''
        if self.checkElementExit('value', item):
            self.value = item['value']
        else:
            self.value = False

        if self.checkElementExit('label', item):
            self.label = item['label']
        else:
            self.label = False

        if self.checkElementExit('infoList', item):
            self.infoList = item['infoList']
        else:
            self.infoList = False

        if self.checkElementExit('image1', item):
            self.image1 = item['image1']
        else:
            self.image1 = False

        if self.checkElementExit('image2', item):
            self.image2 = item['image2']
        else:
            self.image2 = False

    def checkElementExit(self, element, _list) -> bool:
        ''' CHECK IF ELEMENT EXIST IN ITEM '''
        if element in _list:
            return True
        return False 

    def printAsList(self):
        ''' PRINT ITEM AS LIST '''
        _templist = []
        if self.value is not False:
            _templist.append(self.value)

        if self.label is not False:
            _templist.append(self.label)

        if self.infoList is not False:
            _templist.append(self.infoList)
        
        if self.image1 is not False:
            _templist.append(self.image1)

        if self.image2 is not False:
            _templist.append(self.image2)

        print(_templist)

    def printAsXMLItem(self):
        if self.value is not False:
            _localValue = 'value="{value}"'.format(value = self.value)
        
        if self.label is not False:
            _localLabel = 'label="{label}"'.format(label = self.label)

        _localInfoList = str()

        if self.infoList is not False:
            index = 1
            for item in self.infoList:
                _localInfoList = _localInfoList + "info" + str(index) + "=" + '"' + item + '"' + " "
                index = index + 1

        if self.image1 is not False:
            _localImage1 = 'image1="{image1}"'.format(image1 = self.image1)

        if self.image2 is not False:
            _localImage2 = 'image2="{image1}"'.format(image2 = self.image1)

        _XMLOUT = "<ITEM "
        
        if self.value is not False:
            _XMLOUT = _XMLOUT + _localValue + " "

        if self.label is not False:
            _XMLOUT = _XMLOUT + _localLabel + " "
        
        if self.infoList is not False:
            _XMLOUT = _XMLOUT + _localInfoList + " "

        if self.image1 is not False:
            _XMLOUT = _XMLOUT + _localImage1 + " "

        if self.image2 is not False:
            _XMLOUT = _XMLOUT + _localImage2 + " "

        _XMLOUT = _XMLOUT + "/>"
        _XMLOUT = re.sub(' +', ' ', _XMLOUT)
        print(_XMLOUT)

    def returnItemElement(self):
        if self.value is not False:
            _localValue = 'value="{value}"'.format(value = self.value)
        
        if self.label is not False:
            _localLabel = 'label="{label}"'.format(label = self.label)

        _localInfoList = str()

        if self.infoList is not False:
            index = 1
            for item in self.infoList:
                _localInfoList = _localInfoList + "info" + str(index) + "=" + '"' + item + '"' + " "
                index = index + 1

        if self.image1 is not False:
            _localImage1 = 'image1="{image1}"'.format(image1 = self.image1)

        if self.image2 is not False:
            _localImage2 = 'image2="{image1}"'.format(image2 = self.image1)

        _XMLOUT = "<ITEM "
        
        if self.value is not False:
            _XMLOUT = _XMLOUT + _localValue + " "

        if self.label is not False:
            _XMLOUT = _XMLOUT + _localLabel + " "
        
        if self.infoList is not False:
            _XMLOUT = _XMLOUT + _localInfoList + " "

        if self.image1 is not False:
            _XMLOUT = _XMLOUT + _localImage1 + " "

        if self.image2 is not False:
            _XMLOUT = _XMLOUT + _localImage2 + " "

        _XMLOUT = _XMLOUT + "/>"
        _XMLOUT = re.sub(' +', ' ', _XMLOUT)
        return _XMLOUT   