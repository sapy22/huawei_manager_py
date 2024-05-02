import enum




LanguageDict = {
    "English":"en",
    "Arabic":"ar_SA"
    }


DirectionDict = {
    "Left to Right":"ltr",
    "Right to Left":"rtl"
    }


ResolutionDict = {
    "HD":(1280,720)
    }


StyleDict = {
    "RTL Notebook":"rtl.TNotebook",
    "RTL Radiobutton":"rtl.TRadiobutton",
    "RTL Checkbutton":"rtl.TCheckbutton",
    "Hint RTL Checkbutton":"hint.rtl.TCheckbutton"
}

class RTLStyle(enum.Enum):
    RTLNotebook = "rtl.TNotebook"
    RTLRadiobutton = "rtl.TRadiobutton"
    RTLCheckbutton = "rtl.TCheckbutton"
    HintRTLCheckbutton = "hint.rtl.TCheckbutton"