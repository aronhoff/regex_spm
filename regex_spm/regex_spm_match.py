import re
from dataclasses import dataclass
from typing import Callable


@dataclass
class RegexSpmMatch:
  string: str
  _match_func: Callable[[re.Pattern, str], re.Match]
  match: re.Match | None = None

  def __eq__(self, pattern: str | re.Pattern | tuple[str, int | re.RegexFlag]):
    if isinstance(pattern, str):
      pattern = re.compile(pattern)
    elif isinstance(pattern, tuple):
      pattern = re.compile(*pattern)
    self.match = self._match_func(pattern, self.string)
    return self.match is not None

  def __getitem__(
      self,
      group: int | str | tuple[int, ...] | tuple[str, ...]
  ) -> str | tuple[str, ...] | None:
    return self.match[group]
