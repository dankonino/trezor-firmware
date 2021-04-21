# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeInputScriptType = Literal[0, 1, 2, 3, 4]
    except ImportError:
        pass


class GetPublicKey(p.MessageType):
    MESSAGE_WIRE_TYPE = 11

    def __init__(
        self,
        *,
        address_n: Optional[List[int]] = None,
        ecdsa_curve_name: Optional[str] = None,
        show_display: Optional[bool] = None,
        coin_name: str = "Bitcoin",
        script_type: EnumTypeInputScriptType = 0,
        ignore_xpub_magic: Optional[bool] = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.ecdsa_curve_name = ecdsa_curve_name
        self.show_display = show_display
        self.coin_name = coin_name
        self.script_type = script_type
        self.ignore_xpub_magic = ignore_xpub_magic

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('ecdsa_curve_name', p.UnicodeType, None),
            3: ('show_display', p.BoolType, None),
            4: ('coin_name', p.UnicodeType, "Bitcoin"),  # default=Bitcoin
            5: ('script_type', p.EnumType("InputScriptType", (0, 1, 2, 3, 4,)), 0),  # default=SPENDADDRESS
            6: ('ignore_xpub_magic', p.BoolType, None),
        }
