import pygame
import random

class scenaria():
    def __init__(self,x1,x2,y1,y2,scene):
        self.scene=scene
        self.x1=int(x1)
        self.x2=int(x2)
        self.y1=int(y1)
        self.y2=int(y2)

    def checkcoord(self):
        global state
        mouse=pygame.mouse.get_pos()
        scenaria.checkbutton(self)
        scenaria.checkcable(self)
        state=None
        if isButton=='True':
            if (mouse[0]>self.x1 and mouse[0]<self.x2) and (mouse[1]>self.y1 and mouse[1]<self.y2):
                state='ACK'
            else:
                if isCable=='True':
                    state='cable'
                else:
                    state='wrong'
        else:pass
        return state

    def checkcoord2(self):
        global state
        mouse=pygame.mouse.get_pos()
        scenaria.checkbutton2(self)
        scenaria.checkcable2(self)
        state=None
        if isButton=='True':
            if (mouse[0]>self.x1 and mouse[0]<self.x2) and (mouse[1]>self.y1 and mouse[1]<self.y2):
                state='ACK'
            else:
                if isCable=='True':
                    state='cable'
                else:
                    state='wrong'
        else:pass
        return state
       

    def checkbutton(self):
        global isButton
        mouse=pygame.mouse.get_pos()
        isButton='False'
        if (mouse[0]>193 and mouse[0]<271) and (mouse[1]>388 and mouse[1]<432):
            isButton='True'
        elif (mouse[0]>193 and mouse[0]<271) and (mouse[1]>535 and mouse[1]<583):
            isButton='True'
        elif (mouse[0]>523 and mouse[0]<537) and (mouse[1]>113 and mouse[1]<268):
            isButton='True'
        elif (mouse[0]>622 and mouse[0]<637) and (mouse[1]>113 and mouse[1]<268):
            isButton='True'
        elif (mouse[0]>722 and mouse[0]<737) and (mouse[1]>113 and mouse[1]<268):
            isButton='True'
        elif (mouse[0]>822 and mouse[0]<837) and (mouse[1]>113 and mouse[1]<268):
            isButton='True'
        elif (mouse[0]>64 and mouse[0]<152) and (mouse[1]>193 and mouse[1]<260):
            isButton='True'
        elif (mouse[0]>67 and mouse[0]<152) and (mouse[1]>90 and mouse[1]<157) :
            isButton='True'
        elif (mouse[0]>285 and mouse[0]<372) and (mouse[1]>191 and mouse[1]<264):
            isButton='True'
        elif (mouse[0]>283 and mouse[0]<374) and (mouse[1]>87 and mouse[1]<156):
            isButton='True'


    def checkbutton2(self):
        global isButton
        mouse=pygame.mouse.get_pos()
        isButton='False'
        if (mouse[0]>163 and mouse[0]<287) and (mouse[1]>52 and mouse[1]<175) :
            isButton='True'
        elif (mouse[0]>315 and mouse[0]<438) and (mouse[1]>52 and mouse[1]<175) :
            isButton='True'
        elif (mouse[0]>14 and mouse[0]<138) and (mouse[1]>52 and mouse[1]<175):
            isButton='True'
        elif (mouse[0]>150 and mouse[0]<195) and (mouse[1]>385 and mouse[1]<425) :
            isButton='True'
        elif (mouse[0]>207 and mouse[0]<250) and (mouse[1]>385 and mouse[1]<425):
            isButton='True'
        elif (mouse[0]>264 and mouse[0]<306) and (mouse[1]>385 and mouse[1]<425) :
            isButton='True'
        elif (mouse[0]>152 and mouse[0]<195) and (mouse[1]>440 and mouse[1]<483):
            isButton='True'
        elif (mouse[0]>208 and mouse[0]<250) and (mouse[1]>440 and mouse[1]<483) :
            isButton='True'
        elif (mouse[0]>262 and mouse[0]<307) and (mouse[1]>440 and mouse[1]<483):
            isButton='True'
        elif (mouse[0]>152 and mouse[0]<195) and (mouse[1]>499 and mouse[1]<542):
            isButton='True'
        elif (mouse[0]>209 and mouse[0]<252) and (mouse[1]>499 and mouse[1]<542):
            isButton='True'
        elif (mouse[0]>264 and mouse[0]<310) and (mouse[1]>499 and mouse[1]<542):
            isButton='True'
        elif (mouse[0]>151 and mouse[0]<194) and (mouse[1]>556 and mouse[1]<598):
            isButton='True'
        elif (mouse[0]>208 and mouse[0]<252) and (mouse[1]>556 and mouse[1]<598):
            isButton='True'
        elif (mouse[0]>264 and mouse[0]<309) and (mouse[1]>556 and mouse[1]<598):
            isButton='True'
        elif (mouse[0]>574 and mouse[0]<587) and (mouse[1]>112 and mouse[1]<272):
            isButton='True'
        elif (mouse[0]>622 and mouse[0]<636) and (mouse[1]>112 and mouse[1]<272):
            isButton='True'
        elif (mouse[0]>672 and mouse[0]<687) and (mouse[1]>112 and mouse[1]<272):
            isButton='True'
        elif (mouse[0]>723 and mouse[0]<737) and (mouse[1]>112 and mouse[1]<272):
            isButton='True'
        elif (mouse[0]>774 and mouse[0]<789) and (mouse[1]>112 and mouse[1]<272):
            isButton='True'

    def checkcable(self):
        global isCable
        mouse=pygame.mouse.get_pos()
        isCable='False'
        if (mouse[0]>523 and mouse[0]<537) and (mouse[1]>113 and mouse[1]<268):
            isCable='True'
        elif (mouse[0]>622 and mouse[0]<637) and (mouse[1]>113 and mouse[1]<268):
            isCable='True'
        elif (mouse[0]>722 and mouse[0]<737) and (mouse[1]>113 and mouse[1]<268):
            isCable='True'
        elif (mouse[0]>822 and mouse[0]<837) and (mouse[1]>113 and mouse[1]<268):
            isCable='True'
            
    def checkcable2(self):
        global isCable
        mouse=pygame.mouse.get_pos()
        isCable='False'
        if (mouse[0]>574 and mouse[0]<587) and (mouse[1]>112 and mouse[1]<272):
            isCable='True'
        elif (mouse[0]>622 and mouse[0]<636) and (mouse[1]>112 and mouse[1]<272):
            isCable='True'
        elif (mouse[0]>672 and mouse[0]<687) and (mouse[1]>112 and mouse[1]<272):
            isCable='True'
        elif (mouse[0]>723 and mouse[0]<737) and (mouse[1]>112 and mouse[1]<272):
            isCable='True'
        elif (mouse[0]>774 and mouse[0]<789) and (mouse[1]>112 and mouse[1]<272):
            isCable='True'
