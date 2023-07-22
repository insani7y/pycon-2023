# mypy: disable-error-code="attr-defined"
import typing

from mypy.nodes import StrExpr
from mypy.plugin import FunctionContext, Plugin
from mypy.types import Instance, ProperType, Type


class MagicPlugin(Plugin):
    """Gandalf plugin"""

    # Для inference
    def get_function_hook(self, fullname: str) -> typing.Callable[[FunctionContext], Type] | None:
        if "magic_get" in fullname:
            return magic_get_hook
        return None


def magic_get_hook(ctx: FunctionContext) -> Type:
    object_type: Type = ctx.arg_types[0][0]
    attribute_name: str = ctx.args[1][0].value

    if isinstance(object_type, Instance) and isinstance(ctx.args[1][0], StrExpr):
        attr_type = object_type.type.get(attribute_name)
        if attr_type is not None and attr_type.type is not None:
            return attr_type.type

    ctx.api.msg.has_no_attr(object_type, ProperType(), attribute_name, ctx.context)
    return ctx.default_return_type


def plugin(version: str) -> type[Plugin]:
    return MagicPlugin
