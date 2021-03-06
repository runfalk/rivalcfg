_sensitivities = {
    200: 0x04,
    300: 0x06,
    400: 0x08,
    500: 0x0b,
    600: 0x0d,
    700: 0x0f,
    800: 0x12,
    900: 0x14,
    1000: 0x16,
    1100: 0x19,
    1200: 0x1b,
    1300: 0x1d,
    1400: 0x20,
    1500: 0x22,
    1600: 0x24,
    1700: 0x27,
    1800: 0x29,
    1900: 0x2b,
    2000: 0x2e,
    2100: 0x30,
    2200: 0x32,
    2300: 0x34,
    2400: 0x37,
    2500: 0x39,
    2600: 0x3b,
    2700: 0x3e,
    2800: 0x40,
    2900: 0x42,
    3000: 0x45,
    3100: 0x47,
    3200: 0x49,
    3300: 0x4c,
    3400: 0x4e,
    3500: 0x50,
    3600: 0x53,
    3700: 0x55,
    3800: 0x57,
    3900: 0x5a,
    4000: 0x5c,
    4100: 0x5e,
    4200: 0x61,
    4300: 0x63,
    4400: 0x65,
    4500: 0x68,
    4600: 0x6a,
    4700: 0x6c,
    4800: 0x6f,
    4900: 0x71,
    5000: 0x73,
    5100: 0x76,
    5200: 0x78,
    5300: 0x7a,
    5400: 0x7d,
    5500: 0x7f,
    5600: 0x81,
    5700: 0x84,
    5800: 0x86,
    5900: 0x88,
    6000: 0x8b,
    6100: 0x8d,
    6200: 0x8f,
    6300: 0x92,
    6400: 0x94,
    6500: 0x96,
    6600: 0x99,
    6700: 0x9b,
    6800: 0x9d,
    6900: 0xa0,
    7000: 0xa2,
    7100: 0xa4,
    7200: 0xa7,
}


rival110 = {
    "name": "SteelSeries Rival 110",

    "vendor_id": 0x1038,
    "product_id": 0x1729,
    "interface_number": 0,

    "commands": {

        "set_sensitivity1": {
            "description": "Set sensitivity preset 1",
            "cli": ["-s", "--sensitivity1"],
            "command": [0x03, 0x01],
            "suffix": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            "value_type": "choice",
            "choices": _sensitivities,
            "default": 800,
        },

        "set_sensitivity2": {
            "description": "Set sensitivity preset 2",
            "cli": ["-S", "--sensitivity2"],
            "command": [0x03, 0x02],
            "suffix": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            "value_type": "choice",
            "choices": _sensitivities,
            "default": 1600,
        },

        "set_polling_rate": {
            "description": "Set polling rate in Hz",
            "cli": ["-p", "--polling-rate"],
            "command": [0x04, 0x00],
            "suffix": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            "value_type": "choice",
            "choices": {
                125: 0x04,
                250: 0x03,
                500: 0x02,
                1000: 0x01,
            },
            "default": 1000,
        },

        "set_color": {
            "description": "Set the mouse backlight color",
            "cli": ["-c", "--color"],
            "command": [0x05, 0x00],
            "suffix": [0x00, 0x00, 0x00, 0x00],
            "value_type": "rgbcolor",
            "default": "#00FFFF"
        },

        "set_light_effect": {
            "description": "Set the light effect",
            "cli": ["-e", "--light-effect"],
            "command": [0x07, 0x00],
            "suffix": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            "value_type": "choice",
            "choices": {
                "steady": 0x01,
                "breath": 0x03,
                1: 0x01,
                2: 0x02,
                3: 0x03,
                4: 0x04,
            },
            "default": "steady",
        },

        "set_btn6_action": {
            "description": "Set the action of the button under the wheel",
            "cli": ["-b", "--btn6-action"],
            "command": [0x0B],
            "suffix": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            "value_type": "choice",
            "choices": {
                "default": 0x00,
                "os": 0x01,
            },
            "default": "default",
        },

        "save": {
            "description": "Save the configuration to the mouse memory",
            "cli": None,
            "command": [0x09, 0x00],
            "suffix": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            "value_type": None,
        },

    },

}
