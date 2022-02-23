from datetime import timedelta
from typing import (
    ClassVar,
    Type,
    TypeVar,
    overload,
)

import numpy as np

from pandas._libs.tslibs import (
    NaTType,
    Tick,
)
from pandas._typing import npt

_S = TypeVar("_S", bound=timedelta)

def ints_to_pytimedelta(arr: Sequence[int], box: bool = ...) -> np.ndarray: ... 
def array_to_timedelta64(
    values: npt.NDArray[np.object_],
    unit: str | None = ...,
    errors: str = ...,
) -> np.ndarray: ...  # np.ndarray[m8ns]
def parse_timedelta_unit(unit: str | None) -> str: ...
def delta_to_nanoseconds(delta: Tick | np.timedelta64 | timedelta | int) -> int: ...
  
class Timedelta(timedelta):
    min: ClassVar[Timedelta]
    max: ClassVar[Timedelta]
    resolution: ClassVar[Timedelta]
    value: int  # np.int64

    # error: "__new__" must return a class instance (got "Union[Timedelta, NaTType]")
    def __new__(  # type: ignore[misc]
        cls: Type[_S],
        value=...,
        unit: str = ...,
        **kwargs: int | float | np.integer | np.floating,
    ) -> _S | NaTType: ...
    @property
    def days(self) -> int: ...
    @property
    def seconds(self) -> int: ...
    @property
    def microseconds(self) -> int: ...
    def total_seconds(self) -> float: ...
    def to_pytimedelta(self) -> timedelta: ...
    def to_timedelta64(self) -> np.timedelta64: ...
    @property
    def asm8(self) -> np.timedelta64: ...
    # TODO: round/floor/ceil could return NaT?
    def round(self, freq) -> Timedelta: ...
    def ceil(self, freq, **kwargs) -> Timedelta: ...
    def floor(self, freq, **kwargs) -> Timedelta: ...
    @property
    def resolution_string(self) -> str: ...
    def __add__(self, other: timedelta) -> timedelta: ...
    def __radd__(self, other: timedelta) -> timedelta: ...
    def __sub__(self, other: timedelta) -> timedelta: ...
    def __rsub__(self, other: timedelta) -> timedelta: ...
    def __neg__(self) -> timedelta: ...
    def __pos__(self) -> timedelta: ...
    def __abs__(self) -> timedelta: ...
    def __mul__(self, other: float) -> timedelta: ...
    def __rmul__(self, other: float) -> timedelta: ...
    @overload
    def __floordiv__(self, other: timedelta) -> int: ...
    @overload
    def __floordiv__(self, other: int) -> timedelta: ...
    @overload
    def __truediv__(self, other: timedelta) -> float: ...
    @overload
    def __truediv__(self, other: float) -> timedelta: ...
    def __mod__(self, other: timedelta) -> timedelta: ...
    def __divmod__(self, other: timedelta) -> tuple[int, timedelta]: ...
    def __le__(self, other: timedelta) -> bool: ...
    def __lt__(self, other: timedelta) -> bool: ...
    def __ge__(self, other: timedelta) -> bool: ...
    def __gt__(self, other: timedelta) -> bool: ...
    def __hash__(self) -> int: ...
    def isoformat(self) -> str: ...
    def to_numpy(self) -> _np.timedelta64: ...
