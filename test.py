# This file is used to test box drawing issues of the GitHub app on the Android devices.
# It is not meant to be used as a part of any project.

        # ┏━━━━━━━━┯━━━━━━━━┳━━━━━━━━┯━━━━━━━━┓    ┏━━━━━━━━┯━━━━━━━━┯━━━━━━━━┯━━━━━━━━┓
        # ┃ RGBA00 │ RGBA01 ┃ RGBA00 │ RGBA01 ┃    ┃ RGBA00 │ RGBA01 │ RGBA02 │ RGBA03 ┃
        # ┠────────┼────────╂────────┼────────┨    ┠────────┼────────┼────────┼────────┨
        # ┃ RGBA10 │ RGBA11 ┃ RGBA10 │ RGBA11 ┃    ┃ RGBA10 │ RGBA11 │ RGBA12 │ RGBA13 ┃
        # ┠────────┼────────╂────────┼────────┨    ┠────────┼────────┼────────┼────────┨
        # ┃ RGBA20 │ RGBA21 ┃ RGBA20 │ RGBA21 ┃    ┃ RGBA20 │ RGBA21 │ RGBA22 │ RGBA23 ┃
        # ┣━━━━━━━━┿━━━━━━━━╋━━━━━━━━┿━━━━━━━━┫ -> ┠────────┼────────┼────────┼────────┨
        # ┃ RGBA00 │ RGBA01 ┃ RGBA00 │ RGBA01 ┃    ┃ RGBA30 │ RGBA31 │ RGBA32 │ RGBA33 ┃
        # ┠────────┼────────╂────────┼────────┨    ┠────────┼────────┼────────┼────────┨
        # ┃ RGBA10 │ RGBA11 ┃ RGBA10 │ RGBA11 ┃    ┃ RGBA40 │ RGBA41 │ RGBA42 │ RGBA43 ┃
        # ┠────────┼────────╂────────┼────────┨    ┠────────┼────────┼────────┼────────┨
        # ┃ RGBA20 │ RGBA21 ┃ RGBA20 │ RGBA21 ┃    ┃ RGBA50 │ RGBA51 │ RGBA52 │ RGBA53 ┃
        # ┗━━━━━━━━┷━━━━━━━━┻━━━━━━━━┷━━━━━━━━┛    ┗━━━━━━━━┷━━━━━━━━┷━━━━━━━━┷━━━━━━━━┛
        #        (<2>, <2>, <3>, <2>, 4)                       (<6>, <4>, 4)
