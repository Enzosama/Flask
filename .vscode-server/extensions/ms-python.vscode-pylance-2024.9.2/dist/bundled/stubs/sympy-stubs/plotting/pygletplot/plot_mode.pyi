from sympy.plotting.pygletplot.plot_object import PlotObject

class PlotMode(PlotObject):
    intervals = ...
    aliases = ...
    is_default = ...
    def draw(self): ...

    _mode_alias_list = ...
    _mode_map = ...
    _mode_default_map = ...
    def __new__(cls, *args, **kwargs) -> PlotMode: ...

    _was_initialized = ...

def var_count_error(is_independent, is_plotting) -> str: ...
