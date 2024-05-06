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


# "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
# "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
# "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
# "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
# "Chile", "China", "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
# "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
# "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia",
# "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
# "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan",
# "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
# "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia",
# "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
# "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal",
# "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway",
# "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines",
# "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
# "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
# "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia",
# "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
# "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
# "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom",
# "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia",
# "Zimbabwe"

COUNTRIES = ("France","Japan","Kuwait","Russia","Saudi Arabia")


COUNTRIES_MOBILE_OPERATORS = { # prefix to avoid conflict
    "France" : (),
    "Japan" : (),
    "Kuwait" : (),
    "Russia" : (),
    "Saudi Arabia" : ("SA_STC","SA_Mobily","SA_Zain")
}


MOBILE_OPERATORS_BANDS = {
    "SA_STC" : ("b1","b3","b8","b28","b40"),
    "SA_Mobily" : ("b1","b3","b20","b38","b41"),
    "SA_Zain" : ("b1","b3","b8","b20","b38")
}